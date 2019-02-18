from pylibftdi import Device
import time
import numpy as np
import datetime


def get_header():
    header = bytearray()
    header.append(0xff)  # Header
    header.append(0x0b)  # Address, can also be 0x06 and 0x07
    header.append(0xa2)  # Text node
    # Display width
    header.append(0xd0)
    header.append(28)
    # Display height
    header.append(0xd1)
    header.append(16)

    return header

def add_trailer(msg):
    check_sum = 0
    for i in msg[1:]:
        check_sum = check_sum + i

    check_sum = check_sum & 0xff
    if check_sum == 0xfe:
        msg.append(0xfe)
        msg.append(0x00)
    elif check_sum == 0xff:
        msg.append(0xfe)
        msg.append(0x01)
    else:
        msg.append(check_sum)

    msg.append(0xff)

    return msg

def clear_display():
    pix_map = np.zeros([28, 20], dtype=np.bool)

    msg = get_header()

    lines = [5, 10, 15, 20]

    for line in lines:
        # Horizontal offset:
        msg.append(0xd2)
        msg.append(0)

        # Vertical offset:
        msg.append(0xd3)
        msg.append(line-1)

        # Bitmap Font
        msg.append(0xd4)
        msg.append(0x77)

        for horisontal in range(28):
            bit_array = pix_map[horisontal, line-5:line]

            val = sum(bit_array[i] << i for i in range(len(bit_array)))
            val = val | 0x20
            msg.append(val)

    msg = add_trailer(msg)
    return msg

def set_pixels(pixels):
    pix_map = np.zeros([28, 20], dtype=np.bool)
    pix_map[pixels] = True

    mask = np.bitwise_or(pix_map, set_pixels.display_state)
    set_pixels.display_state = pix_map.copy()

    msg = get_header()
    lines = [5, 10, 15, 20]
    for line in lines:
        # Vertical offset:
        msg.append(0xd3)
        msg.append(line-1)

        # Bitmap Font
        msg.append(0xd4)
        msg.append(0x77)

        horisontal_skip = True
        for horisontal in range(28):
            if mask[horisontal, line-5:line].any():
                # Horizontal offset:
                if horisontal_skip:
                    msg.append(0xd2)
                    msg.append(horisontal)
                    horisontal_skip = False

                bit_array = pix_map[horisontal, line-5:line]

                val = sum(bit_array[i] << i for i in range(len(bit_array)))
                val = val | 0x20

                msg.append(val)
            else:
                horisontal_skip = True

    msg = add_trailer(msg)
    return msg


set_pixels.display_state = np.zeros([28, 20], dtype=np.bool)


def write(text):
    msg = get_header()

    # Horizontal offset:
    msg.append(0xd2)
    msg.append(3)

    # Vertical offset:
    msg.append(0xd3)
    msg.append(11)

    # Font
    msg.append(0xd4)
    msg.append(0x75) #0x75  #0x65 0x66

    msg.extend(text.encode('utf-8'))

    msg = add_trailer(msg)
    return msg


with Device(mode='b') as dev:
    dev.baudrate = 4800

    while True:
        time_now = datetime.datetime.now()
        time_str = time_now.strftime("%H:%M")
        msg = write(time_str)
        dev.write(msg)
        time.sleep(10)
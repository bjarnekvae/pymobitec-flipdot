from pylibftdi import Device
import time
import numpy as np

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

def set_pixels(pixels):
    pix_map = np.zeros([28, 20], dtype=np.bool)
    pix_map[pixels] = True

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

            #print(bit_array)

            val = sum(bit_array[i] << i for i in range(len(bit_array)))
            val = val | 0x20
            #print(val)
            msg.append(val)



    # Pixel value, 0x20 in all off, 0x3f is all on
    #val = 0x20
    #msg.append(val)
    #print(bin(val))

    msg = add_trailer(msg)

    return msg


def write(text):
    msg = get_header()

    # Horizontal offset:
    msg.append(0xd2)
    msg.append(1)

    # Vertical offset:
    msg.append(0xd3)
    msg.append(6)

    # Font
    msg.append(0xd4)
    msg.append(0x75)

    msg.extend(text.encode('utf-8'))

    msg = add_trailer(msg)

    return msg


with Device(mode='b') as dev:
    dev.baudrate = 4800

    seq = tuple([[0,1,2,3,4,5,6,7,8,9], [0,1,2,3,4,5,6,7,8,9]])

    for y in range(16):
        for x in range(28):
            msg = set_pixels(tuple([x, y]))
            dev.write(msg)
    quit()

    time.sleep(1)

    msg = write("HEI")
    dev.write(msg)


from pylibftdi import Device
import time


def add_checksum(msg):
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

    return msg


def write(text):
    msg = bytearray()
    msg.append(0xff)
    msg.append(0x0b)
    msg.append(0xa2)

    msg.extend(text.encode('utf-8'))

    msg = add_checksum(msg)

    msg.append(0xff)

    return msg


with Device(mode='b') as dev:
    dev.baudrate = 4800

    for i in range(11):
        msg = write(str(i))
        dev.write(msg)
        time.sleep(1)

    quit()

    packet = bytearray()
    #packet.append(0xff)
    #packet.append(0x07)
    #packet.append(0xa2)

    packet.append(0xd2)
    packet.append(1)
    packet.append(0xd3)
    packet.append(4)
    packet.append(0xd4)
    packet.append(0x77)
    for i in range(28):
        packet.append(0x3f)

    packet.append(0x00)
    print(packet)

    dev.write(packet)

    print(dev.read(len(packet)))

    #test = bytearray()
    #test.append(0xff)

    #while True:
    #   dev.write(test)
    #    print(dev.read(len(packet)))
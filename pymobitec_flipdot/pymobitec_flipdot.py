import numpy as np

_numbers_14px = {
    "0": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1,
        2, 2, 2, 2,
        3, 3, 3, 3,
        4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
       [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        1, 2, 13, 14,
        1, 2, 13, 14,
        1, 2, 13, 14,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
    "1": [[1,
        2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [2,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]],
    "2": [[0, 0, 0, 0, 0, 0, 0,
        1, 1, 1, 1, 1, 1, 1,
        2, 2, 2, 2, 2, 2, 2,
        3, 3, 3, 3, 3, 3, 3,
        4, 4, 4, 4, 4, 4],
       [2, 3, 10, 11, 12, 13, 14,
        1, 2, 9, 10, 11, 13, 14,
        1, 2, 7, 8, 9, 13, 14,
        1, 2, 5, 6, 7, 13, 14,
        2, 3, 4, 5, 13, 14]],
    "3": [[0, 0, 0, 0,
          1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
         [2, 3, 12, 13,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          2, 3, 4, 5, 6, 9, 10, 11, 12, 13]],
    "4": [[0, 0, 0, 0,
         1, 1, 1, 1, 1,
         2, 2, 2, 2, 2,
         3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
         4, 4],
         [7, 8, 9, 10,
         5, 6, 7, 9, 10,
         3, 4, 5, 9, 10,
         1, 2, 3, 8, 9, 10, 11, 12, 13, 14,
         9, 10]],
    "5": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2,
         3, 3, 3, 3, 3, 3,
         4, 4, 4, 4, 4, 4, 4, 4],
         [1, 2, 3, 4, 5, 6, 7, 8, 12, 13,
         1, 2, 7, 8, 13, 14,
         1, 2, 7, 8, 13, 14,
         1, 2, 7, 8, 13, 14,
         1, 2, 8, 9, 10, 11, 12, 13]],
    "6": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4, 4, 4],
          [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          2, 3, 8, 9, 10, 11, 12, 13]],
    "7": [[0, 0,
          1, 1, 1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2,
          3, 3, 3, 3, 3,
          4, 4, 4, 4, 4],
          [1, 2,
          1, 2, 9, 10, 11, 12, 13, 14,
          1, 2, 7, 8, 9,
          1, 2, 5, 6, 7,
          1, 2, 3, 4, 5]],
    "8": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          1, 1, 1, 1, 1, 1,
          2, 2, 2, 2, 2, 2,
          3, 3, 3, 3, 3, 3,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
          [2, 3, 4, 5, 6, 9, 10, 11, 12, 13,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          1, 2, 7, 8, 13, 14,
          2, 3, 4, 5, 6, 9, 10, 11, 12, 13]],
    "9": [[0, 0, 0, 0, 0, 0, 0, 0,
         1, 1, 1, 1, 1, 1,
         2, 2, 2, 2, 2, 2,
         3, 3, 3, 3, 3, 3,
         4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
         [2, 3, 4, 5, 6, 7, 12, 13,
         1, 2, 7, 8, 13, 14,
         1, 2, 7, 8, 13, 14,
         1, 2, 7, 8, 13, 14,
         2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]],
    ":": [[0, 0, 0, 0,
          1, 1, 1, 1],
          [4, 5, 10, 11,
          4, 5, 10, 11]],
    ".": [[0, 0,
           1, 1],
          [13, 14,
           13, 14]]
}

class Fonts:
    text_5px = 0x72  # Large letters only
    text_6px = 0x66
    text_7px = 0x65
    text_7px_bold = 0x64
    text_9px = 0x75
    text_9px_bold = 0x70
    text_9px_bolder = 0x62
    text_13px = 0x73
    text_13px_bold = 0x69
    text_13px_bolder = 0x61
    text_13px_boldest = 0x79
    numbers_14px = 0x00
    text_15px = 0x71
    text_16px = 0x68
    text_16px_bold = 0x78
    text_16px_bolder = 0x74
    symbols = 0x67
    bitwise = 0x77

class Text:
    def __init__(self, text, horizontal=0, vertical=0, font=Fonts.text_5px):
        self.text = text
        self.horizontal = horizontal
        self.vertical = vertical
        self.font = font

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


def _set_pixels(msg, pixels):
    pix_map = np.zeros([28, 20], dtype=np.bool)
    pix_map[pixels] = True

    mask = np.bitwise_or(pix_map, _set_pixels.display_state)
    _set_pixels.display_state = pix_map.copy()

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

    return msg


_set_pixels.display_state = np.zeros([28, 20], dtype=np.bool)


def _set_text(msg, text_str, horizontal_offset, vertical_offset, font):
    # Horizontal offset:
    msg.append(0xd2)
    msg.append(horizontal_offset)

    # Vertical offset:
    msg.append(0xd3)
    msg.append(vertical_offset)

    # Font
    msg.append(0xd4)
    msg.append(font)

    msg.extend(text_str.encode('utf-8'))
    return msg


def set_text_and_pixels(text_str, horizontal_offset, vertical_offset, font, pixels):
    msg = get_header()

    msg = _set_pixels(msg, pixels)
    msg = _set_text(msg, text_str, horizontal_offset, vertical_offset, font)

    msg = add_trailer(msg)
    return msg


def set_pixels(pixels):
    msg = get_header()

    msg = _set_pixels(msg, pixels)

    msg = add_trailer(msg)
    return msg


def set_text(text_str, horizontal_offset, vertical_offset, font):
    msg = get_header()

    if font == Fonts.numbers_14px:
        pixels_x = []
        pixels_y = []
        x_offset = horizontal_offset
        y_offset = vertical_offset
        for char in text_str:
            number = _numbers_14px[char].copy()
            width = max(_numbers_14px[char][:][0])
            pixels_x += [x + x_offset for x in number[:][0]]
            pixels_y += [y + y_offset for y in number[:][1]]
            x_offset += width + 2

        pixels = tuple([pixels_x, pixels_y])
        msg = _set_pixels(msg, pixels)
    else:
        msg = _set_text(msg, text_str, horizontal_offset, vertical_offset, font)

    msg = add_trailer(msg)
    return msg


def set_texts(text_list):
    msg = get_header()

    while len(text_list) > 0:
        text_object = text_list.pop(0)

        # Horizontal offset:
        msg.append(0xd2)
        msg.append(text_object.horizontal)

        # Vertical offset:
        msg.append(0xd3)
        msg.append(text_object.vertical)

        # Font3
        msg.append(0xd4)
        msg.append(text_object.font)

        msg.extend(text_object.text.encode('utf-8'))

    msg = add_trailer(msg)
    return msg


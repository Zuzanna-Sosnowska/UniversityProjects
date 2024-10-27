
def rgb2hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def hex2rgb(hexcode: str) -> (int, int, int):
    return tuple(int(hexcode[i:i+2], 16) for i in (1, 3, 5))


if __name__ == '__main__':
    print(rgb2hex(2, 7, 23))            #przykładowy kolor
    print(hex2rgb(rgb2hex(2, 7, 23)))

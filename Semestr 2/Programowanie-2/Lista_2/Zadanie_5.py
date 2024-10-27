from PIL import Image


def watermark(path1: str, path2: str, size_x: int, size_y: int, x: int, y: int, new_name: str):
    """
    :param path1: ścieżka do zdjęcia, do którego zostanie dodany znak wodny (obrazek nr1)
    :param path2: ścieżka do zdjęcia, które będzie znakiem wodnym (obrazek nr2)
    :param size_x: szerokość zdjęcia, które będzie znakiem wodnym
    :param size_y: wysokość zdjęcia, które będzie znakiem wodnym
    :param x: współrzędna x położenia obrazka który będzie znakiem wodnym
    :param y: współrzędna y położenia obrazka który będzie znakiem wodnym
    :param new_name: nazwa, pod którą zostanie zapisany obrazek
    :return: obrazek ze znakiem wodnym
    """
    image_1 = Image.open(path1)
    image_2 = Image.open(path2)
    # rozmiar obrazka nr1
    size = (size_x, size_y)
    # tworzenie miniatury z obrazka nr2
    image_2.thumbnail(size)
    # zmienianie transparentności obrazka nr2
    image_2.putalpha(50)
    # wklejanie obrazka nr2 na obrazek nr1 w miejscu współrzędnych (x, y)
    image_1.paste(image_2, (x, y), mask=image_2)
    # zapisywanie obrazka pod nową nazwą zadaną jako parametr 'new_name'
    image_1.save(f'{new_name}')

watermark('krajobraz2.png', 'panda.png', 200, 200, 300, 200, 'znak_wodny.png')

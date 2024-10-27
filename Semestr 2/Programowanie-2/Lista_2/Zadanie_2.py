from PIL import Image


def picture_thumbnail(path, name, x: int = 100, y: int = 100):
    """
    :param path: ścieżka do obrazka
    :param name: nazwa zminiaturyzowanego obrazka
    :param x: szerokość miniatury
    :param y: wysokość miniatury
    :return: miniatura obrazka
    """
    image = Image.open(path)
    # określamy rozmiary miniatury
    size = (x, y)
    # tworzymy miniaturę
    image.thumbnail(size)
    # zapisujemy miniaturę
    image.save(f'{name}.png')
    # pokazujemy miniaturę
    image.show()

picture_thumbnail("krajobraz.jpg", 'miniatura', 200, 100)

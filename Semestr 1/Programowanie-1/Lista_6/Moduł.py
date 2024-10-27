import random


def kolizja(k1: (float, float, float), k2: (float, float, float)) -> bool:
    if (k1[0] - k2[0])**2 + (k1[1] - k2[1])**2 >= (k1[2] + k2[2])**2:
        return False
    return True


def przesun_dysk(w: (float, float), k: (float, float, float)) -> (float, float, float):
    return k[0] + w[0], k[1] + w[1], k[2]


def losowy_dysk(min_x: float, min_y: float, max_x: float, max_y: float) -> (float, float, float):
    x = random.uniform(min_x, max_x)
    y = random.uniform(min_y, max_y)
    return x, y, 0.5


def main():
    k1 = (1, 1, 1)
    k2 = (3, 2, 1)
    print(kolizja(k1, k2))
    print(przesun_dysk((2, 3), k1))


if __name__ == '__main__':
    print(losowy_dysk(1, -2, 12, 34))
    print(kolizja((-2,-5,1), (-1,0,1)))
    print(przesun_dysk((-3, 7), (2, 1, 4)))


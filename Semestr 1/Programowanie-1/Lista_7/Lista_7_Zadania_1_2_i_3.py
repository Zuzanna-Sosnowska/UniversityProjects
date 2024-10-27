import math
import random
import matplotlib.pyplot as plt


class Rocket:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b

    def get_position(self):
        return self.x, self.y

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


if __name__ == '__main__':

    r = Rocket(random.random(), random.random())
    p = Rocket(random.random(), random.random())

    print(r.get_position())
    print(p.get_position())

    print(r.get_distance(p))

    r.move(5, 7)
    print(r.get_position())

    rakiety = [Rocket(random.random(), random.random()) for _ in range(5)]

    for idx in range(len(rakiety)):
        rakieta = rakiety[idx]
        j = idx + 1
        print(idx + 1)
        while j < len(rakiety):
            rakieta2 = rakiety[j]
            print(rakieta.get_distance(rakieta2))
            j += 1

    x = []
    y = []
    for Rocket in rakiety:
        x0, y0 = Rocket.get_position()
        x.append(x0)
        y.append(y0)

    plt.scatter(x, y)
    plt.show()

    rakiety[0].move(2.1, 7.3)
    x = []
    y = []
    for rakieta in rakiety:
        x0, y0 = rakieta.get_position()
        x.append(x0)
        y.append(y0)

    plt.scatter(x, y)
    plt.show()




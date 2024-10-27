import Moduł as m
import matplotlib.pyplot as plt
import random


def main():
    dyski = [m.losowy_dysk(-14.5, -14.5, 14.5, 14.5) for _ in range(325)]
    circles = []
    for dysk in dyski:
        circles += [plt.Circle((dysk[0], dysk[1]), dysk[2], color='blue')]
    fig, ax = plt.subplots()
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    for circle in circles:
        ax.add_patch(circle)
    plt.show()

    kolidujace = []
    for i in range(len(dyski)):
        for j in range(i+1, len(dyski)):
            (x1, y1, r1) = dyski[i]
            (x2, y2, r2) = dyski[j]
            if abs(x1 - x2) < 1 and abs(y1 - y2) < 1:
                if m.kolizja(dyski[i], dyski[j]):
                    kolidujace += [(i, j)]

    calkowite = {}
    tmp_x = -14.5
    tmp_y = -14.5
    for i in range(30):
        for j in range(30):
            s = (tmp_x, tmp_y)
            calkowite[s] = True
            tmp_x += 1
        tmp_x = -14.5
        tmp_y += 1

    for dysk in dyski:
        (x, y, r) = dysk
        s = (x, y)
        if s in calkowite:
            calkowite[(x, y)] = False
        else:
            x = int(x + 0.5) if x > 0 else int(x - 0.5)
            y = int(y + 0.5) if y > 0 else int(y - 0.5)

            calkowite[(x + 0.5, y + 0.5)] = False
            calkowite[(x + 0.5, y - 0.5)] = False
            calkowite[(x - 0.5, y + 0.5)] = False
            calkowite[(x - 0.5, y - 0.5)] = False

    wolne = [pole for pole in calkowite if calkowite[pole]]
    random.shuffle(wolne)

    for i in range(len(kolidujace)):
        (dysk1_idx, dysk2_idx) = kolidujace[i]
        (x, y, r) = dyski[dysk1_idx]
        (new_x, new_y) = wolne[i]
        dyski[dysk1_idx] = (new_x, new_y, r)

    circles2 = []
    for dysk in dyski:
        circles2 += [plt.Circle((dysk[0], dysk[1]), dysk[2], color='red')]
    fig2, ax2 = plt.subplots()
    ax2.set_xlim(-15, 15)
    ax2.set_ylim(-15, 15)
    for circle in circles2:
        ax2.add_patch(circle)
    plt.show()


if __name__ == '__main__':
    main()

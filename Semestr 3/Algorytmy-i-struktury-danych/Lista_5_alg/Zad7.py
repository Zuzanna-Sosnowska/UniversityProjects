import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import numpy as np
from PIL import Image
from io import BytesIO

help_arr = []
states = []


def mergesort(arr):
    global help_arr
    help_arr = arr.copy()
    states.append(arr.copy())
    merge(arr, 0, len(arr) - 1)
    return arr


def merge(arr, low, high):
    global help_arr
    center = (low + high) // 2
    if high - low <= 0:
        return
    merge(arr, low, center)
    merge(arr, center + 1, high)
    i = low
    j = center + 1
    k = low
    while i <= center and j <= high:
        if arr[i] <= arr[j]:
            help_arr[k] = arr[i]
            i += 1
        else:
            help_arr[k] = arr[j]
            j += 1
        k += 1
        states.append(help_arr.copy())

    while i <= center:
        help_arr[k] = arr[i]
        i += 1
        k += 1
        states.append(help_arr.copy())
    while j <= high:
        help_arr[k] = arr[j]
        j += 1
        k += 1
        states.append(help_arr.copy())
    for k in range(low, high + 1):
        arr[k] = help_arr[k]


# Funkcja generująca wykres
def create_plot(x, y):
    plt.bar(x, y)
    plt.ylim(np.min(x) - 1, np.max(x) + 1)

    image_bytes = BytesIO()
    plt.savefig(image_bytes, format='png')
    plt.close()
    return image_bytes.getvalue()

def animate(arr, values):
    frames = []
    for y in values:
        frame = create_plot(arr, y)
        frames.append(Image.open(BytesIO(frame)))

    # Tworzenie gifa
    gif_bytes = BytesIO()
    frames[0].save(
        gif_bytes,
        format='GIF',
        save_all=True,
        append_images=frames[1:],
        duration=20,
        loop=0
    )

    with open('mergesort.gif', 'wb') as f:
        f.write(gif_bytes.getvalue())


n = 100
arr = np.arange(n) + 1
random.shuffle(arr)
mergesort(arr)
animate(np.arange(n) + 1, states)

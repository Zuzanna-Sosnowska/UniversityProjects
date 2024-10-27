import os
import random


def createDirAndFiles(path, file_prob, dir_prob,  depth=3):
    if depth == 0:
        return
    a = 5
    b = 1
    c = 1
    while a != 0:
        if file_prob >= random.random():
            new_path = os.path.join(path, f"file{b}.txt")
            b += 1
            with open(new_path, 'w'):
                pass
        if dir_prob >= random.random():
            new_path = os.path.join(path, f"directory{c}")
            c += 1
            os.mkdir(new_path)
            createDirAndFiles(new_path, file_prob, dir_prob, depth-1)
        a -= 1


parent_dir = "C:\\Users\\Zuzia\\PycharmProjects\\pythonProject3\\Lista2algorytmy"
new_path = os.path.join(parent_dir, "directory")
os.mkdir(new_path)

createDirAndFiles(new_path, 0.5, 0.25)

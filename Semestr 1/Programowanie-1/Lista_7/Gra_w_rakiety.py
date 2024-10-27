from tkinter import *
from PIL import ImageTk, Image
import random

GAME_WIDTH = 600
GAME_HEIGHT = 550
SPACE_SIZE = 50
NUMBER_OF_ROCKETS = 3
ROCKET_COLOR = "#00FF00"
DISK_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
SCIEZKA = ".\\rakiety\\"


class Rocket:

    def __init__(self):
        self.number_of_rockets = NUMBER_OF_ROCKETS
        self.coordinates = []
        self.squares = []

        for i in range(0, NUMBER_OF_ROCKETS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_image(x, y, anchor=NW, image=rakiety["down"])
            self.squares.append(square)
            #rakieta_label = Label(image=rakieta_tk)
            #rakieta_label.image = rakieta_tk
            #rakieta_label.place(x=x, y=y+window_height-GAME_HEIGHT)
            #square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=ROCKET_COLOR, tag="rakiety")


class Disks:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=DISK_COLOR, tag="food")


def next_turn(rocket, kierunek):
    global disk
    x, y = rocket.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    rocket.coordinates.insert(0, (x, y))

    # tu trzeba zmienic na ddanie obrazka
    square = canvas.create_image(x, y, anchor=NW, image=rakiety[kierunek])
    #square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=ROCKET_COLOR)

    rocket.squares.insert(0, square)

    if x == disk.coordinates[0] and y == disk.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        disk = Disks()

    else:

        del rocket.coordinates[-1]

        canvas.delete(rocket.squares[-1])

        del rocket.squares[-1]

    if check_collisions(rocket):
        game_over()


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
        else:
            return
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
        else:
            return
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
        else:
            return
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction
        else:
            return
    window.after(0, next_turn, rocket, new_direction)


def check_collisions(rocket):

    x, y = rocket.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in rocket.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red")


window = Tk()
window.title("Rocket game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack(expand=YES, fill=BOTH)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

rakiety = {}
for kierunek in ["up", "down", "left", "right"]:
    rakieta = Image.open(SCIEZKA + kierunek + ".png")
    rakieta = rakieta.resize((SPACE_SIZE, SPACE_SIZE))
    rakiety[kierunek] = ImageTk.PhotoImage(rakieta)

rocket = Rocket()
disk = Disks()
window.mainloop()

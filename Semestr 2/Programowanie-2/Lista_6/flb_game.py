# niezbędne importy
import random
import sys
import pygame
import pygame_menu
from pygame.locals import *

# zapisywanie 5 najlepszych wyników do pliku tekstowego
def dumpLeaderboardToFile():
    lb = open('leaderboard.txt', 'w')
    for score in leaderboard_list:
        lb.write(f'{score};')
    lb.close()

# Pobieranie wcześniejszych najlepszych wyników z pliku tekstowego
def leaderboardFromFile():
        lb = open('leaderboard.txt', 'r')
        line = lb.read()
        lb.close()
        if line == '':
            return []
        scores_str = line.split(';')
        scores_str.pop()
        scores = list(map(lambda x: int(x), scores_str))
        return scores


# ustawienia początkowe - szerokość i wysokość ekranu
window_width = 500
window_height = 500

# pobieranie ostatniej listy 5 najlepszych wyników
leaderboard_list = leaderboardFromFile()

# ustawianie szerokości i wysokości okna
window = pygame.display.set_mode((window_width, window_height))
scores_widget = None
elevation = window_height * 0.8
game_images = {}
# ilość klatek na sekundę
framepersecond = 32
framepersecond_clock = pygame.time.Clock()

# ustawienie obrazków
lollipop_image = 'C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\lizaczek.png'
background_image = 'C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\tlo.png'
unicorn_image = 'C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\jednorug.png'
sealevel_image = 'C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\base.jpg'


def flappygame():
    # ustawianie parametrów początkowych - wynik, położenie początkowe jednorożca
    your_score = 0
    horizontal = int(window_width / 5)
    vertical = int(window_width / 2)
    ground = 0
    mytempheight = 100

    # generowanie lizaków - górnego i dolnego
    first_loli = createLollipop()
    second_loli = createLollipop()

    # lista zawierająca dolne lizaki
    down_lollipops = [
        {
            'x': window_width + 300 - mytempheight,
            'y': first_loli[1]['y']
        },
        {
            'x': window_width + 300 - mytempheight + (window_width / 2),
            'y': second_loli[1]['y']
        },
    ]

    # lista zawierająca górne lizaki
    up_lollipops = [
        {
            'x': window_width + 300 - mytempheight,
            'y': first_loli[0]['y']
        },
        {
            'x': window_width + 200 - mytempheight + (window_width / 2),
            'y': second_loli[0]['y']
        },
    ]

    # prędkość poruszania się lizaka
    lollipopVelX = -4

    # prękość jednorożca
    unicorn_velocity_y = -9
    unicorn_Max_Vel_Y = 10
    unicorn_Min_Vel_Y = -8
    unicornAccY = 1

    unicorn_flap_velocity = -8
    unicorn_flapped = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                # jeśli użytkownik będzie chciał zakończyć grę, to muzyka się wyłączy a gracz wróci do menu
                pygame.mixer.quit()
                game_menu.mainloop(surface)

            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if vertical > 0:
                    unicorn_velocity_y = unicorn_flap_velocity
                    unicorn_flapped = True

        # sprawdzamy w pętli, czy jednorożec nie uderzył w lizaka
        game_over = isGameOver(horizontal, vertical, up_lollipops, down_lollipops)
        if game_over:
            # jeśli użytkownik uderzy w lizaka to dodajemy jego wynik do listy najlepszych wyników, sortujemy, a następnie usuwamy ostatni element z listy
            leaderboard_list.append(your_score)
            leaderboard_list.sort(reverse=True)
            if len(leaderboard_list) > 5:
                leaderboard_list.pop()
            dumpLeaderboardToFile()
            return

        # sprawdzamy wynik
        playerMidPos = horizontal + game_images['flappybird'].get_width() / 2
        for loli in up_lollipops:
            loliMidPos = loli['x'] + game_images['pipeimage'][0].get_width() / 2
            if loliMidPos <= playerMidPos < loliMidPos + 4:
                your_score += 1

        if unicorn_velocity_y < unicorn_Max_Vel_Y and not unicorn_flapped:
            unicorn_velocity_y += unicornAccY

        if unicorn_flapped:
            unicorn_flapped = False
        playerHeight = game_images['flappybird'].get_height()
        vertical = vertical + min(unicorn_velocity_y, elevation - vertical - playerHeight)

        # przesuwanie lizaków w lewo
        for upperLolli, lowerLolli in zip(up_lollipops, down_lollipops):
            upperLolli['x'] += lollipopVelX
            lowerLolli['x'] += lollipopVelX

        # dodawanie nowego lizaka
        if 0 < up_lollipops[0]['x'] < 5:
            newlolli = createLollipop()
            up_lollipops.append(newlolli[0])
            down_lollipops.append(newlolli[1])

        # usuwanie lizaków, które ominął jednorożec
        if up_lollipops[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_lollipops.pop(0)
            down_lollipops.pop(0)

        window.blit(game_images['background'], (0, 0))
        for upperLolli, lowerLolli in zip(up_lollipops, down_lollipops):
            window.blit(game_images['pipeimage'][0], (upperLolli['x'], upperLolli['y']))
            window.blit(game_images['pipeimage'][1], (lowerLolli['x'], lowerLolli['y']))

        window.blit(game_images['sea_level'], (ground, elevation))
        window.blit(game_images['flappybird'], (horizontal, vertical))

        # Wyświetlanie wyniku
        numbers = [int(x) for x in list(str(your_score))]
        width = 0

        for num in numbers:
        	width += game_images['scoreimages'][num].get_width()
        Xoffset = (window_width - width)/1.1

        for num in numbers:
        	window.blit(game_images['scoreimages'][num],
        				(Xoffset, window_width*0.02))
        	Xoffset += game_images['scoreimages'][num].get_width()

        # Odświeżanie wyniku

        pygame.display.update()
        framepersecond_clock.tick(framepersecond)


def isGameOver(horizontal, vertical, up_lolli, down_lolli):
    if vertical > elevation - 25 or vertical < 0:
        return True

    for lolly in up_lolli:
        lolliHeight = game_images['pipeimage'][0].get_height()
        if vertical < lolliHeight + lolly['y'] and \
                abs(horizontal - lolly['x']) < game_images['pipeimage'][0].get_width():
            return True

    for lolly in down_lolli:
        if (vertical + game_images['flappybird'].get_height() > lolly['y']) and \
                abs(horizontal - lolly['x']) < game_images['pipeimage'][0].get_width():
            return True
    return False


def createLollipop():
    offset = window_height / 3
    lolliHeight = game_images['pipeimage'][0].get_height()
    y2 = offset + random.randrange(0, int(window_height - game_images['sea_level'].get_height() - 1 * offset))

    lolliX = window_width + 10
    y1 = lolliHeight - y2 + offset
    lolli = [
        # górny lizak
        {'x': lolliX, 'y': -y1},

        # dolny lizak
        {'x': lolliX, 'y': y2}
    ]
    return lolli


def main_loop():
    pygame.init()
    pygame.display.set_caption('Flappy Bird Game')
    pygame.mixer.music.load('game_music.mp3')
    pygame.mixer.music.play(-1)
    # ładowanie obrazków do gry
    leaderboard_list = leaderboardFromFile()

    # obrazki z cyframi przedstawiającymi wynik
    game_images['scoreimages'] = (pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\zero.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\one.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\two.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\three.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\four.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\five.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\six.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\seven.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\eight.png').convert_alpha(),
    	pygame.image.load('C:\\Users\\Zuzia\\PycharmProjects\\pythonProject6\\Lista_6\\img\\nine.png').convert_alpha())

    game_images['flappybird'] = pygame.image.load(unicorn_image).convert_alpha()
    game_images['sea_level'] = pygame.image.load(sealevel_image).convert_alpha()
    game_images['background'] = pygame.image.load(background_image).convert_alpha()
    game_images['pipeimage'] = (pygame.transform.rotate(pygame.image.load(lollipop_image)
                                                        .convert_alpha(), 180),
                                pygame.image.load(lollipop_image).convert_alpha())

    # Główna pętla
    while True:
        # ustawiamy położenie początkowe jednorożca
        horizontal = int(window_width / 5)
        vertical = int((window_height - game_images['flappybird'].get_height()) / 2)
        ground = 0

        while True:
            for event in pygame.event.get():

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    onQuit()

                elif event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                    flappygame()

                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'], (horizontal, vertical))
                    window.blit(game_images['sea_level'], (ground, elevation))
                    pygame.display.update()
                    framepersecond_clock.tick(framepersecond)


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((window_width, window_height))
    # konfuguracja meu - zmiana suwaka, czcionki, itp.
    theme_menu = pygame_menu.themes.THEME_BLUE.copy()
    theme_menu.scrollbar_cursor = pygame_menu.locals.CURSOR_HAND
    theme_menu.widget_font = pygame_menu.font.FONT_COMIC_NEUE
    theme_menu.title_font = pygame_menu.font.FONT_COMIC_NEUE
    theme_menu.title_bar_style = pygame_menu.widgets.MENUBAR_STYLE_SIMPLE

    game_menu = pygame_menu.Menu('Flappy unicorn', window_width, window_height,
                                 theme=theme_menu)
    about_menu = pygame_menu.Menu('O Autorze', window_width, window_height,
                                  theme=theme_menu)
    rules_menu = pygame_menu.Menu('Zasady gry', window_width, window_height,
                                  theme=theme_menu)
    leader_menu = pygame_menu.Menu('Najlepsze wyniki', window_width, window_height,
                                   theme=theme_menu)

    about_menu.add.label('Jestem studentką pierwszego roku politechniki wrocławskiej. Gra "Flappy Unicorn" została przeze mnie stworzona na laboratoria z programowania. Liczę, że zostanie ona pozytywnie odebrana.',
        max_char=33, align=pygame_menu.locals.ALIGN_LEFT, margin=(0, -1))
    about_menu.add.button('Powrót', pygame_menu.events.BACK)
    rules_menu.add.label('Zasady gry\n\n Głównym celem gry jest zdobycie jak największej ilości punktów. Punkty zdobywa się pokonując przeszkody z lizaków, znajdujące się zarówno u góry, jak i na dole planszy. Przemieszczają się one w czasie w stronę jednorożca. Położenie jednorożca możemy kontrolować - po wciśnięciu spacji lub strzałki w górę jednorożec poruszy się w górę, natomiast nie wciskanie klawiszów sprawi, że jednorożec poruszy się w dół. Gra kończy się w momencie, gdy jednorożec uderzy w rurę. Aby powrócić do menu należy wcisnąć przycisk Esc.',
        max_char=33, align=pygame_menu.locals.ALIGN_LEFT, margin=(0, -1))
    rules_menu.add.button('Powrót', pygame_menu.events.BACK)

    scores_str = ''
    for score in leaderboard_list:
        scores_str += f'Player score: {score: 3d}\n'

    scores_widget = leader_menu.add.label(f'{scores_str}')[0]
    leader_menu.add.button('Powrót', pygame_menu.events.BACK)

    game_menu.add.button('Play', main_loop)
    game_menu.add.button('O autorze', lambda: game_menu._open(about_menu))
    game_menu.add.button('Zasady gry', lambda: game_menu._open(rules_menu))
    game_menu.add.button('Najlepsze wyniki', lambda: game_menu._open(leader_menu))
    game_menu.add.button('Wyjście', pygame_menu.events.EXIT)
    game_menu.mainloop(surface)

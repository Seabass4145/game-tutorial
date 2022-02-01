from pygame import *
from fighter import *
from config import *
from health import *

pygame.init()
mixer.init()

mixer.music.load('Adventure.mp3')
mixer.music.set_volume(0.7)

clock = pygame.time.Clock()
fps = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Battle')

# define fonts
font = pygame.font.SysFont('Times New Roman', 26)

# load images
# background image
background_img = pygame.image.load('img/Background/background.png').convert_alpha()
# panel image
panel_img = pygame.image.load('img/Icons/panel.png').convert_alpha()

# import sound
fuckS = pygame.mixer.Sound('SCREAM_4.mp3')


# function to draw text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# function for drawing the background
def draw_bg():
    screen.blit(background_img, (0, 0))


# Function for drawing Panel
def draw_panel():
    # draw panel rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))
    # show knights stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, blue, 100, screen_height - bottom_panel + 10)
    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)


knight = Fighter(200, 260, 'Knight', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)

# mixer.music.play(-1)
running = True
while running:

    clock.tick(fps)

    # draw background
    draw_bg()

    # draw panel
    draw_panel()
    knight_health_bar.draw(knight.hp, screen)
    bandit1_health_bar.draw(bandit1.hp, screen)
    bandit2_health_bar.draw(bandit2.hp, screen)

    # draw fighters
    knight.update()
    knight.draw(screen)
    for bandit in bandit_list:
        bandit.update()
        bandit.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()

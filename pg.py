import pygame as pg
import random
import math
from pygame import mixer
pg.init()
screen = pg.display.set_mode((800,600))

score_val =0
font = pg.font.SysFont('comicsansms',32)
over_font = pg.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_val), True, (0, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
mixer.music.load('/Users/a./Downloads/Undertale - Megalovania.mp3')
mixer.music.play(-1)
pg.display.set_caption("SPACE INVADERS")
icon = pg.image.load("/Users/a./Downloads/spaceship.png")
waveImg = pg.image.load("/Users/a./Downloads/bullet.png")
# enemy = pg.image.load("/Users/a./Downloads/spaceship (1).png")
pg.display.set_icon(icon)
running = True
player_X = 370
player_Y = 480
player_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 15

for i in range(num_of_enemies):
    enemyImg.append(pg.image.load('/Users/a./Downloads/spaceship (1).png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 300))
    enemyX_change.append(0.5)
    enemyY_change.append(40)
wave_X = 0
wave_Y = 480
wave_state = "ready"
# wave_X_change =0.5
wave_Y_change = 2
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def player(icon,x,y):
    screen.blit(icon,(x,y))
def wave(waveImg,x,y):
    global wave_state
    wave_state = "fire"
    screen.blit(waveImg,(x,y))

def isCollision(enemy_X,enemy_Y,wave_X,wave_Y):
    distance = math.sqrt((math.pow(enemy_X-wave_X,2)+math.pow(enemy_Y-wave_Y,2)))
    if distance<=35:
        return True
    else:
         return False
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player_change = -3
            if event.key == pg.K_RIGHT:
                player_change = 3
            if event.key == pg.K_SPACE:
                if wave_state == "ready":
                    wave_X = player_X
                    bullet_sound = mixer.Sound('/Users/a./Downloads/Laser Gun Sound Effect.mp3')
                    bullet_sound.play()
                    wave(waveImg,wave_X,wave_Y)
        if event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT or pg.K_LEFT:
                player_change = 0
    screen.fill((75,25,35))
    player_X += player_change
    if player_X<0:
        player_X=0
        #Taking in consideration size of space ship 800-64=736
    elif player_X>736:
        player_X=736
    for i in range(num_of_enemies):
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], wave_X, wave_Y)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_val += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

    if wave_Y <=0:
        wave_state = "ready"
        wave_Y = 480
    if wave_state ==  "fire":
        wave(waveImg,wave_X,wave_Y)
        wave_Y -= wave_Y_change





    player(icon,player_X,player_Y)
    show_score(10,10)
    pg.display.update()

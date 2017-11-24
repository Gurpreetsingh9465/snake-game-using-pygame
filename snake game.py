import pygame
from pygame.locals import *
import sys
import random
import time
from pygame import event
#from event import keyword
errors = pygame.init()
if errors[1] > 0:
    print("errors occurs so exit....")
    sys.exit()
else:
    print("Pygame is running")
canvas = pygame.display.set_mode((720, 460)) # canvas creation
pygame.display.set_caption(" snake game by gurpreet singh")
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 25, 45)
fps = pygame.time.Clock()
score = 0
snakeposition = [100, 50]
snakebody = [[100, 50], [90, 50], [80, 50]]
foodposition = [random.randrange(1, 72)*10, random.randrange(1, 46)*10]
foodfound = True
direction = 'RIGHT'
changeto = direction
def gameover():
    # for making code take the reference
    font = pygame.font.SysFont('monaco', 72)
    GOsurf = font.render('Game Over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 0)
    canvas.blit(GOsurf, GOrect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() # pygame
    sys.exit() # console
def showscore(choice = 1):
    sfont = pygame.font.SysFont('monaco', 50)
    ssurf = sfont.render('SCORE:'+str(score), True, black)
    srect = ssurf.get_rect()
    if choice == 1:
        srect.midtop = (80, 10)
    else:
        srect.midtop = (360, 120)
    canvas.blit(ssurf, srect)
    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    #valid of direction
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snakeposition[0] +=10
    if direction == 'LEFT':
        snakeposition[0] -=10
    if direction == 'UP':
        snakeposition[1] -=10
    if direction == 'DOWN':
        snakeposition[1] +=10


    # body expansion

    snakebody.insert(0, list(snakeposition))
    if snakeposition[0] == foodposition[0] and snakeposition[1] == foodposition[1]:
        score += 1
        foodfound = False
    else:
        snakebody.pop()
    if foodfound == False:
        foodposition = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodfound = True
    canvas.fill(white)
    for pos in snakebody:
        pygame.draw.rect(canvas, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(canvas, brown, pygame.Rect(foodposition[0], foodposition[1], 10, 10))
    if snakeposition[0] > 710 or snakeposition[0] < 0:
        showscore(0)
        gameover()

    if snakeposition[1] > 450 or snakeposition[1] < 0:
        showscore(0)
        gameover()

    for block in snakebody[1:]:
        if snakeposition[1] == block[0] and snakeposition[1] == block[1]:
            showscore(0)
            gameover()


    pygame.display.flip()
    showscore()
    fps.tick(20)



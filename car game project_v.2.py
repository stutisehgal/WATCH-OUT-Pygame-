#-------------------------------------------------------------------------------
# Name:        WATCH OUT
# Purpose:
#
# Author:      User
#
# Created:     11/02/2017
# Copyright:   (c) User 2017
# Licence:     <STUTI SEHGAL>
#-------------------------------------------------------------------------------
def main():
    pass
if __name__ == '__main__':
    main()

#to create a game: WATCH OUT (where u have to dodge blocks)
import pygame
import time
import random
import sys
from pygame.locals import *
pygame.init()

#size of screen
display_width = 800
display_height = 600

#defining colours
background_colour = (255,206,245)
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
block_color = (255,206,245)

gameDisplay = pygame.display.set_mode((display_width,display_height))     #screen size
gameDisplay.fill(background_colour)                                 #Background Colour
pygame.display.set_caption('WATCH OUT')               #give a title to the game window
clock = pygame.time.Clock()

#about the car
car_width = 73
carImg = pygame.image.load('C:\Users\User\Documents\juhi\cs\py game project\car_edit.png')

#to count the number of dodges
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, black)
    gameDisplay.blit(text,(0,0))

#creating blocks
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x,y):                                                     #putting car on screen
    gameDisplay.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#losing the game
def crash():
    message_display('GAME OVER')

#makimg the blocks fall again and again using random function
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 4
    thing_width = 100
    thing_height = 100

    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)


        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.2)

        if y < thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
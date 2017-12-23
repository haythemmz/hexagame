
import pygame
import sys
import board
import pygame.gfxdraw
import cls
import functions
import corps
import colors
from test import paus
from corps import lis
from test import talwin
from ML import filpos,test_gain,a
m=lis()

pygame.init()
gameDisplay = pygame.display.set_mode((800,600))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()


crashed = False

board.drow_bord()
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

        #pygame.Surface.set_at((10,10),black)        pygame.gfxdraw.pixel(gameDisplay, 100, 50, black)
        if event.type == pygame.MOUSEBUTTONDOWN:

            x=pygame.mouse.get_pos()
            print(x)
            for k in m :
                if paus(x,k) ==1 :
                    #print(k)
                    talwin(k)
                    print("index est {}".format(m.index(k)))
                    b=a
                    b=filpos(a,m.index(k),1)
                    if test_gain(a,1)==1:
                        print("blach wins ")

                    #print(b)




    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()

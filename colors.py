import functions
import pygame
import sys
import board
import pygame.gfxdraw
import cls
import alwan

gameDisplay = pygame.display.set_mode((800,600))

def sub (x,y):


            for i in range(0, 200, 20):

                    if functions.line(i, 15, i+10,5,x,y )==0:
                        pygame.gfxdraw.pixel(gameDisplay, i, i+10, alwan.black)



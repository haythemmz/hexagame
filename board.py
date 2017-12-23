import pygame
import random, pygame, sys
from pygame.locals import *
import  math
import functions
def drow_bord():
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)

    gameDisplay=pygame.display.set_mode((200,155))
    gameDisplay.fill(white)
    b=5
    a=0
    while(a<300):

        l = []
        m = []
        n = []
        p = []
        for i in range(0, 11):
            l.append([2 * 10 *i, 10+a+b])
            m.append([2 * i * 10 + 10, 0+a+b])
            pygame.draw.line(gameDisplay, red, tuple(l[i]), tuple(m[i]), 1)
            n.append([2 * 10 * i, 20+a+b])
            p.append([2 * i * 10 + 10, 30+a+b])
            pygame.draw.line(gameDisplay, red, tuple(n[i]), tuple(p[i]), 1)

        for i in range(0, len(m) - 1):
            pygame.draw.line(gameDisplay, red, tuple(m[i]), tuple(l[i + 1]), 1)
        for i in range(0, len(p) - 1):
            pygame.draw.line(gameDisplay, red, tuple(p[i]), tuple(n[i + 1]), 1)
        for i in range(0, 11):
            pygame.draw.line(gameDisplay, red, (i * 20, 10+a+b), (i * 20, 20+a+b), 1)
        a=a+40
    print(300-a)
    for i in range(0,11):
        pygame.draw.line(gameDisplay, red, (i * 20+10,0), (i * 20+10, 5), 1)

    for i in range(0,11):
        for j in range (0,11):
            pygame.draw.line(gameDisplay, red, (i * 20+10,35+40*j), (i * 20+10, 45+40*j), 1)

    for i in range(200):
        for j in range(155):
            if functions.line(0, 15, 10, 5, i, j) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, black)

    for x in range(10, 200, 20):
        for i in range(200):
            for j in range(155):
                if functions.line(x, 5, x + 10, 15, i, j) == 0 and functions.line(x + 10, 15, x + 20, 5, i, j) == 0:
                    pygame.gfxdraw.pixel(gameDisplay, i, j, black)

    for i in range(200):
        for j in range(155):
            if functions.line(0, 145, 10, 155, i, j) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, black)

    for x in range(10, 200, 20):
        for i in range(200):
            for j in range(155):
                if functions.line(x, 155, x + 10, 145, i, j) == 1 and functions.line(x + 10, 145, x + 20, 155, i,j) == 1:
                    pygame.gfxdraw.pixel(gameDisplay, i, j, black)
    """

    for z in range(0, 50, 10):
        for i in range(200):
            for j in range(155):
                if functions.line(z, z + 25, z + 10, z + 35, i, j) == 1 and functions.vert(z+10 , i) == 1:
                    pygame.gfxdraw.pixel(gameDisplay, i, j, red)

        """
    for i in range(200):
        for j in range(155):
            if functions.line(0, 25, 10, 35, i, j) == 1 and functions.vert(10, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(10, 45, 20, 55, i, j) == 1 and functions.vert(20, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(20, 65, 30, 75, i, j) == 1 and functions.vert(30, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(30, 85, 40, 95, i, j) == 1 and functions.vert(40, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(40, 105, 50, 115, i, j) == 1 and functions.vert(50, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(50, 125, 60, 135, i, j) == 1 and functions.vert(60, i) == 1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(200, 135, 190, 125, i, j) == 0 and functions.vert(190, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(190, 115, 180, 105, i, j) == 0 and functions.vert(180, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(180, 95, 170, 85, i, j) == 0 and functions.vert(170, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(170, 75, 160, 65, i, j) == 0 and functions.vert(160, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(160, 55, 150, 45, i, j) == 0 and functions.vert(150, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)
    for i in range(200):
        for j in range(155):
            if functions.line(150, 35, 140, 25, i, j) == 0 and functions.vert(140, i) == 0:
                pygame.gfxdraw.pixel(gameDisplay, i, j, red)





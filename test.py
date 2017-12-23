
import pygame
import sys
import board
import pygame.gfxdraw
from corps import  lis
from alwan import black
from alwan import red
from alwan import white

gameDisplay = pygame.display.set_mode((800,600))

m=lis()
board.drow_bord()
def paus (x,l):
    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]
    e=l[4]
    f=l[5]
    var=0
    point=(a[1]-b[1])/(a[0]-b[0])
    coff = a[1] - point * a[0]

    if (point*x[0]+coff<x[1]):
        var=1
    else:
        return 0

    point = (a[1] - c[1]) / (a[0] - c[0])
    coff = a[1] - point * a[0]

    if (point*x[0]+coff<x[1]):
        var=1
    else:
        return 0

    point = (d[1] - f[1]) / (d[0] - f[0])
    coff = d[1] - point * d[0]

    if (point * x[0] + coff > x[1]):
        var = 1
    else:
        return 0

    point = (e[1] - f[1]) / (e[0] - f[0])
    coff = e[1] - point * e[0]

    if (point * x[0] + coff > x[1]):
        var = 1
    else:
        return 0


    if b[0]>x[0] and c[0]<x[0]:
        var=1
    else:
        var=0
    return var

def talwin(l):
    for i in range(200):
        for j in range (155):
            x=(i,j)

            if paus(x,l)==1:
                pygame.gfxdraw.pixel(gameDisplay, i, j, black)




l=[[60, 25], [70, 35], [50, 35], [70, 45], [50, 45], [60, 55]]
#talwin(l)

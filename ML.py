import numpy as np
#from test import paus
#from corps import lis
#import pygame
#from board import drow_bord



a=np.zeros((11,11))




def filpos (a,k,chiffre):
    x=k//7
    y=k%7
    a[x+2,y+2]=chiffre
    return a

def test_gain(a,chiffre):
    b=a
    for k in range(11):
        if (b[2,k]==chiffre ):
            b[2,k]=-1

    for i in range(2,9):
        for j in range (2,9):
            if b[i,j]==chiffre and ( b[i-1,j]==-1 or b[i-1,j+1]==-1 or b[i,j+1]==-1  or b[i,j-1]==-1):# a corrigé
                b[i,j]=-1


    for p in range (9):
        if b[8,p]==-1:
            return 1

    return 0





"""
for i in range (0,7):
    x=int(input("donne l'abssaice de la {} point".format(i)))
    y=int(input("donner l'ordonné de la {} point".format(i)))
    a[x+1,y+1]=1


print(a)

print(test_gain(a,1))
"""
a[1,7]=2
print(a)
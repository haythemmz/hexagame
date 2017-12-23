import pygame



def limnite (a,b,c,d,x,y):
    if x>a and x<b and y>c and y<d :
        return 1
    else:
        return 0


def line(a,b,c,d,x,y):
    point=(b-d)/(a-c)
    coff=b-point*a
    if (point*x+coff<y):
        return 1
    else:
        return 0
def vert(a,x):
    if (x<a):
        return 1
    else:
        return 0


"""
def choix(m,a,b):
    
    for event in pygame.event.get():
        # pygame.Surface.set_at((10,10),black)        pygame.gfxdraw.pixel(gameDisplay, 100, 50, black)
        if event.type == pygame.MOUSEBUTTONDOWN:
            x = pygame.mouse.get_pos()
    
    l=[]
    #a=x
    #b=y
    #for i in m:

    
    for i in m:
        print(len(i))
        #if line(i[0][0],i[0][1],i[1][0],i[1][1],a,b)==1 and line(i[0][0],i[0][1],i[2][0],i[2][1],a,b)==1 and vert(i[1][0],a)==1 and vert(i[2][0],a)==0 and line(i[3][0],i[3][1],i[5][0],i[5][1],a,b)==0 and line(i[4][0],i[4][1],i[5][0],i[5],[1],a,b)==0:
        if vert(i[1][0],a)==1:
            l.append(i)
    return l


#print(choix(100,100))
print(choix(m,100,100))
print(len(choix(m,100,100)))
    """
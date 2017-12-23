import numpy as np
""""
b=[]
for i in range(0, 7):
    allo = []
    for j in range(0, 7):
        allo.append((i + 1) * 10 + j * 20)
    b.append(allo)


#b = np.array(allo).reshape(7, 7)
#print(b [5][6])

#print(b[0,2])
x=[]
c=[]
for j in range(0, 7):
    x.append(5)
c.append(x)
for i in range(1, 7):
    x=[]
    for j in range(0, 7):
        x.append(i * 20 + 5)
    c.append(x)

#c = np.array(x).reshape(7, 7)

#print(c[0][1])
#print(len(c))


#print(" shape".format(np.shape(b)))

m = []
l = []
k = 0


for i in range(7):
    w = b[i]
    print(w[5])

#print(m)
#k=np.array([np.array(xi) for xi in m])
#k=np.vstack(m)
#print(k.shape)



#m=print(lud(b,c))
"""
def lis ():
    l=[]
    m=[]
    for i in range(7):
        for j in range(7):
            x = (i + 1) * 10 + j * 20
            if i == 0:
                y = 5
            else:
                y = i * 20 + 5

            l.append([x, y])
            a = x + 10
            b = y + 10
            l.append([a, b])
            c = x - 10
            d = y + 10
            l.append([c, d])
            e = x + 10
            f = y + 20
            l.append([e, f])
            h = x - 10
            o = y + 20
            l.append([h, o])
            p = x
            q = y + 30
            l.append([p, q])
            # print(l)
            # print("\n")
            m.append(l)
            l = []

    return (m)

print(lis())
class hexa:

    def __int__(self,a):
        self.a=a
        self.b=[a[0]+10,a[1]+10]
        self.c =[a[0]-10,a[1]+10]
        self.d =[a[0]+10,a[1]+20]
        self.e = [a[0]-10,a[1]+20]
        self.f = [a[0],a[1]+30]



    def explace(self,p):
        """"
        point =(self.a[1]-self.b[1])/(self.a[0]-self.b[1])
        ordo=self.a[1]-point*self.a[0]
        if ( p[0]*point+ordo < p[1]):
            bol_1=1
        else:
            bol_1=0
        """
        if (p[0]<self.b[0]) :
            bol_2=1
        else:
            bol_2=0


        point = (self.d[1] - self.f[1]) / (self.d[0] - self.f[1])
        ordo = self.d[1] - point * self.d[0]
        if ( p[0]*point+ordo < p[1]):
            bol_3=1
        else:
            bol_3=0
        """
        
        point = (self.f[1] - self.e[1]) / (self.f[0] - self.e[1])
        ordo = self.f[1] - point * self.f[0]
        if ( p[0]*point+ordo < p[1]):
            bol_4=1
        else:
            bol_4=0
        
        if (p[0]>self.c[0]) :
            bol_5=1
        else:
            bol_5=0

        point = (self.a[1] - self.c[1]) / (self.a[0] - self.c[1])
        ordo = self.a[1] - point * self.a[0]
        if (p[0] * point + ordo < p[1]):
            bol_6 = 1
        else:
            bol_6 = 0
        """
        #if bol_1*bol_2*bol_3*bol_4*bol_5*bol_6 ==1 :
        if bol_2*bol_3==1:
            return 1
        else:
            return 0



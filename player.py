# -*- coding: utf-8 -*-

class Player:

    XMAX = None
    YMAX = None

    def __init__ (self,name,height,weight,xmax,ymax):

        self.name = str(name)
        self.h = float(height)
        self.w = float(weight)
        self.speed = (1000-abs(self.h-110-self.w))*(self.h+160*(1-self.h/240))/10000

        self.
        self.x = 0
        self.y = 0
        self.a = 0 # arm's angle

        XMAX = xmax
        YMAX = ymax

        self.has_ball = False

    def occupied (noob):

        if abs(noob.x-self.x)< and abs(noob.y-self.y)< :

            return True

        #if x y are free
        return False

    def moove_ok (x,y) :

        if x >= XMAX :
            return False

        if y >= YMAX :
            return False

        if not occupied(x,y) :
            return True


    def moove (self,x,y,a):

        if x == self.x and y == self.y:

            self.a = a

        elif a == self.a :

            #check if collide with wall or player
            self.x = x
            self.y = y

        #return (x,y,a)


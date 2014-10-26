# -*- coding: utf-8 -*-

from threading import Thread
import subprocess as sp


class Interface(Thread):
    
    def __init__(self, p1, p2):
        self.p1 = sp.Popen(p1,stdin=sp.PIPE, stdout=sp.PIPE)
        self.p2 = sp.Popen(p2,stdin=sp.PIPE, stdout=sp.PIPE)
        print p1.stdout
        print p2.stdout
    
    def getData(self):
        return {"RED":{},"BLUE":{}}
        
    def listen(self):
        pass

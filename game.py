# -*- coding: utf-8 -*-
from arena import * 
from interface import * 

class Game:
    
    def __init__(self):
        
        self.interface = Interface("./basket","./basket")
        data = self.interface.getData()
        
        self.arena = Arena(data)
    
    def play(self):
        print 'yeah'

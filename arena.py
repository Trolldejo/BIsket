# -*- coding: utf-8 -*-
 
from player import * 
from threading import Thread

class Arena(Thread):
    """
    """
    
    XMAX = 800
    YMAX = 600
    
    def __init__(self, data):
        """
        """
        self.red  = {}
        self.blue = {}
        self.init_players(data)
    
    def init_players(self, data):
        """
        """
        d = data["RED"]
        for i in d:
            self.red[i]   = Player(d[i]["name"],d[i]["height"],d[i]["weight"],XMAX, YMAX)
            self.red[i].x = d[i]["x"]
            self.red[i].y = d[i]["y"]
            self.red[i].a = 0
        d = data["BLUE"]
        for i in d:
            self.blue[i]   = Player(d[i]["name"],d[i]["height"],d[i]["weight"],XMAX, YMAX)
            self.blue[i].x = d[i]["x"]
            self.blue[i].y = d[i]["y"]
            self.blue[i].a = 180
    
    def move_players(self, mvt, col):
        """
        """
        team = None
        if col == "RED":
            team = self.red
        else:
            team = self.blue
        for i in mvt:
            ret += team[i["name"]].move(i["mvt"])
        return ret
    
    def reverseData(self, data):
        """
        """
        for i in data:
            data[i]["x"]  =  XMAX - data[i]["x"]
            data[i]["y"]  =  YMAX - data[i]["y"]
            data[i]["a"] += (-180 if data[i]["a"] >= 180 else 180)
        return data
    
    def reverseAll(self, data):
        """
        """
        for i in data:
            data[i] = self.reverseData(data[i])
    
    

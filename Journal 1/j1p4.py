# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:59:55 2026

@author: mimi
"""

class Crow:
    def __init__(self):
        self.name = "Hooded Crow"
        self.sciName = "Corvus cornix"
        self.wingspan = 41.0 #inches
        self.legLength = 3.0 #inches
        self.eyeCount = 2
        self.hasTail = True
        self.isFurry = False
    
    def print(self):
        tail = "no"
        furry = "not "
        if self.hasTail:
            tail = "a"
        if self.isFurry:
            furry = ""
        print(f"The {self.name} ({self.sciName}) has a wingspan of {self.wingspan} inches", end =" ")
        print(f"and a leg length of {self.legLength} inches. It has {self.eyeCount}", end = " ")
        print(f"eyes and has {tail} tail and is {furry}furry.")
        
def main():
    bird = Crow()
    bird.print()

if __name__ == "__main__":
    main()
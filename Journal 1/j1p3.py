# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:57:46 2026

@author: mimi
"""

def mathematicalFunction(x):
    returnValue = x**3
    returnValue += 8
    return returnValue

def main():
    value = mathematicalFunction(9)
    print(value)
    if(value > 27):
        print("YAY!")

if __name__ == "__main__":
    main()
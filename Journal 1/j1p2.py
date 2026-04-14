# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:56:27 2026

@author: mimi
"""

def printPrompt2Floats(float1, float2):
    #make sure float1 and float2 are actually floats
    float1 = float(float1)
    float2 = float(float2)
    print(f"{float1} + {float2} = {float1 + float2} and is data type {type(float1 + float2)}")

def printPrompt2Ints(int1, int2):
    #make sure int1 and int2 are actually ints
    int1 = int(int1)
    int2 = int(int2)
    print(f"{int1} - {int2} = {int1 - int2} and is data type {type(int1 - int2)}")

def printPrompt2Product(int1, float1):
    #make sure int1 and float1 are the correct variable types
    int1 = int(int1)
    float1 = float(float1)
    print(f"{int1} * {float1} = {int1 * float1} and is data type {type(int1 * float1)}")
    
def main():
    printPrompt2Floats(5, 34.5324)
    printPrompt2Ints(3, 5.4)
    printPrompt2Product(2, "3.54")

if __name__ == "__main__":
    main()
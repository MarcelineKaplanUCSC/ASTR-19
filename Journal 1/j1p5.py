# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 12:02:09 2026

@author: mimi
"""

from astropy.table import Table
import numpy as np





def prompt5():
    x = np.linspace(0,2.0 * np.pi,1000) #create a data array of x from 0 to 2PI with 1000 steps
    y = np.sin(x) #create a data array of sin(x)
    promptTable = Table([x,y],names=['x','sin(x)']) #create our table
    print(promptTable) #print the table

def main():
    prompt5()

if __name__ == "__main__":
    main()
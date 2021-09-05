#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 10:41:10 2021

@author: romanregmi
"""

import random

#initialize snakes and ladder
snake_ladder ={1:38, 4:14, 8:30, 28:76, 21:42, 50:67, 71:92, 80:99, 62:18, 36:6, 32:10, 88:24, 95:56, 97:78}



a = 0
b = 10

#create a grid for reference
gridline = [i for i in range(100,0,-1)]
grid = []

for i in range(10):
    grid.append(list(gridline[a:b]))
    a = a + 10
    b = b + 10
        
#simulate the grid to match the actual borad game
for i in range(10):
    if(i%2!=0):
        grid[i].reverse()


#initial position
pointer = 0

#count of the number of steps
step = 0


#main code
while(pointer!=100):
    step=step+1

    possiblilities = random.randint(1, 6)
    pointer = pointer + possiblilities

    if (pointer in snake_ladder.keys()):
        pointer=snake_ladder[pointer]

    if (pointer>100):
        pointer=pointer-possiblilities
        
print("The number of steps it took was ", step)
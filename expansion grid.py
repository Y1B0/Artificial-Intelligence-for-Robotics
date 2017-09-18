# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 11:36:16 2017

@author: huyibo
"""

# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space
from operator import add
import numpy as np
import copy
grid = [[0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
footprint = [init]
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search():
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = [0,init[0],init[1]]
    archive = copy.deepcopy(grid)
    grid[init[0]][init[1]] = 1
    expand = [[-1 for i in range(len(grid[0]))]for j in range(len(grid))]
    expand[init[0]][init[1]] = 0
    track = [[' ' for i in range(len(grid[0]))]for j in range(len(grid))]
    track[goal[0]][goal[1]] = "*"
    def is_valid(maze,curr):
        if curr[0]>=len(maze) or curr[0]<0 or curr[1]>=len(maze[0]) or curr[1]<0:
            return False
        elif maze[curr[0]][curr[1]] == 1:
            return False
        else:
            return True
    
    stack = [path]
    next_level = []
    step_record = 0
    found = False
    while stack or next_level:
        if not stack:
            stack = next_level
            next_level = []
        curr_path = stack.pop(0)
#        print curr_path
        curr_position = [curr_path[1],curr_path[2]]
        if curr_position == goal:
#            print np.matrix(expand)
            found = True
            break

        for i,step in enumerate(delta):
            next_step = map(add,step,curr_position)
            if is_valid(grid,next_step):
                grid[next_step[0]][next_step[1]] = 1
                step_record += 1
                expand[next_step[0]][next_step[1]] = step_record
                next_level.append([curr_path[0]+cost,next_step[0],next_step[1],delta_name[i]])
    tracked = False
    def minimal_prev(curr):
        record = []
        fake_delta_name = ['v', '>', '^', '<']
        for i,step in enumerate(delta):
            prev_step = map(add,step,curr)
            if (is_valid(archive,prev_step)) and (expand[prev_step[0]][prev_step[1]] > -1):
                record.append([prev_step[0],prev_step[1],fake_delta_name[i]])
        mini = record[0]
        for i in record:
            if expand[i[0]][i[1]]<expand[mini[0]][mini[1]]:
                mini = i
        return mini
    if found:
        curr = goal
        while not tracked:
#            print curr
            if curr == init:
                tracked = True
                break
            prev_step = minimal_prev(curr)
            curr = [prev_step[0],prev_step[1]]
            track[prev_step[0]][prev_step[1]] = prev_step[2]
        print np.matrix(expand)
        print np.matrix(track)
        return track
    return "fail"


search()
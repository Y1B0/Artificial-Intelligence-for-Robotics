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
import sys

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1
footprint = [init]
delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']


def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    path = [0,init[0],init[1]]
    def is_valid(grid,curr):
        if curr[0]>=len(grid) or curr[0]<0 or curr[1]>=len(grid[0]) or curr[1]<0:
            return False
        elif grid[curr[0]][curr[1]] == 1:
            return False
        else:
            return True
    
    stack = [path]
    next_level = []
    while stack:
        curr_path = stack.pop(0)
        print curr_path
        curr_position = [curr_path[1],curr_path[2]]
#        grid[curr_position[0]][curr_position[1]] = 1
        if curr_position == goal:
            return curr_path
        if not stack:
            stack = next_level
            next_level = []
        for step in delta:
            next_step = map(add,step,curr_position)
            if is_valid(grid,next_step):
                grid[next_step[0]][next_step[1]] = 1
                stack.append([curr_path[0]+cost,next_step[0],next_step[1]])
    return "fail"


print search(grid,init,goal,cost)
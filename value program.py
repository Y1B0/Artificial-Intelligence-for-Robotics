# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
import numpy as np
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for i in range(len(grid[0]))]for j in range(len(grid))]
#    for i,row in enumerate(grid):
#        for j,elem in enumerate(row):
#            if elem == 1:
#                value[i][j] = 99

    finish = False
    e = [0,goal[0],goal[1]]
    q = [e]
    closed = []
    def valid(c,p):
        # c is closed matrix
        # p stands for current position
#        print p
#        print "and"
#        print c
        if p[0]>=len(grid) or p[0]<0 or p[1]>=len(grid[0]) or p[1]<0:
            return False
        if grid[p[0]][p[1]] == 1 or (p in c):

            return False
        return True
    
    while q:
#        q.sort()
        curr = q.pop(0) # current [value,position]
#        print curr
        pos = [curr[1],curr[2]] # current position
        value[curr[1]][curr[2]] = curr[0]
        closed.append([curr[1],curr[2]])
        for orie in delta:
            npos = [pos[0] + orie[0],pos[1] + orie[1]] # next position
            if valid(closed,npos):
                q.append([curr[0]+1,npos[0],npos[1]]) # next value
#                print [curr[0]+1,npos[0],npos[1]]
        
        
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
print np.matrix(compute_value(grid,goal,cost))
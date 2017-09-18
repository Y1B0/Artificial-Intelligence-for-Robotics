# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 11:26:54 2017

@author: huyibo
"""
s = "cbbd"
dp = [[0 for i in range(len(s))]for i in range(len(s))]
for i in range(len(s)):
    dp[i][i] = 1
for i in range(len(s)-1):
    row = i+1
    for j in range(0,len(s)-1-i):
        row = j
        col = j+1+i
        print row, 
        print col
        if(s[i] == s[j]):
            dp[row][col] = dp[row+1][col-1]+2
        else:
            dp[row][col] = max(dp[row+1][col],dp[row][col-1])

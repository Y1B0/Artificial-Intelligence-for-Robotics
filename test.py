# -*- coding: utf-8 -*-
"""
Created on Thu Sep 07 10:33:21 2017

@author: huyibo
"""
prices = [1,2,4,3,2,6,3,4]
min_val = 9999
max_rev = 0
forward = []
for i in prices:
    min_val = min(min_val,i)
    max_rev = max(max_rev,i-min_val)
    forward.append(max_rev)
max_val = -9999
max_rev = 0
backward = []
for i in reversed(prices):
    max_val = max(max_val,i)
    max_rev = max(max_rev,max_val - i)
    backward.append(max_rev)
res = 0
for k in range(len(prices)):
    res = max(res,forward[k]+backward[len(prices)-k-1])
print res
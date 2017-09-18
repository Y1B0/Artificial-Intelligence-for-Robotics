# -*- coding: utf-8 -*-
"""
Created on Wed Sep 06 14:57:20 2017

@author: huyibo
"""

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dp = [[0 for i in range(l)]for j in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for i in range(1,l):
            for j in range(i,l):
                if s[j-i] == s[j]:
                    dp[j-i][j]=dp[j-i+1][j-1]+2
                else:
                    dp[j-i][j]=max(dp[j-i][j-1],dp[j-i+1][j])
        return dp[0][l-1]
    
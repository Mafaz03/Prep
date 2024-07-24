# https://www.naukri.com/code360/problems/longest-common-subsequence_1063255

from os import *
from sys import *
from collections import *
from math import *

def getLengthOfLCS(str1, str2):
    dp = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(len(str1)-1, -1, -1):
        for j in range(len(str2)-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
    return dp[0][0]

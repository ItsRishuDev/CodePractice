"""
Given an integer N, return the number of digits in N.
"""

import math


def countDigit(n: int):
    return int(math.log10(n) + 1)


# Brute force approach
# def countDigit(n: int):
#     count = 0
#     while n > 0:
#         n = n//10
#         count+=1
#     return count


print(countDigit(564546))

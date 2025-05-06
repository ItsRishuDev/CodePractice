"""
Prime Number
"""

from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.

def check_prime(n):
    count = 0
    sqr_rt_n = int(n ** 0.5)

    for i in range(1, sqr_rt_n+1):
        if n%i == 0:
            count+=1
            if n/i != i:
                count+=1
        

        if count > 2: 
            return "NO"

    return "YES" if count == 2 else "NO"

if __name__ == '__main__':
    n = int(input())
    print(check_prime(n))
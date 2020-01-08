#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    non = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            pos += 1
        
        elif arr[i] == 0:
            non += 1
        
        else :
            neg += 1
        
    print(format(pos/len(arr), '.6f'))
    print(format(neg/len(arr), '.6f'))
    print(format(non/len(arr), '.6f'))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
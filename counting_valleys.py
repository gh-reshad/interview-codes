import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    down = 0
    up = 0
    sum = 0
    valley = 0
    mountain = 0
    for i in range(n):
        if s[i] == 'D':
            down = down - 1
        
        if s[i] == 'U':
            up = up + 1
        
        sum = up + down
        if sum == 0:
            if s[i] == 'U':
                valley += 1
            
            if s[i] == 'D':
                mountain += 1
    
    return valley


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input().rstrip().split(' ')

    result = countingValleys(n, s)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

import math
import re
import sys
import random
import numpy as np


def jumpingOnClouds(c):
    jump = 0
    i = 0
    while i < len(c) - 1 :
        if c[i+1] == 0:
            if i+2 < len(c) -1 and c[i+2] == 0:
                jump += 1
                i = i + 2
            else:
                jump += 1
                i = i + 1
        else:
            jump += 1
            i = i + 2

    return jump




if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
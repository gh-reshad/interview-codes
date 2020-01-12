import math
import os
import random
import re
import sys
import numpy as np

def rotLeft(a, d):
    #temp = a
    # temp = []
    # for j in range(len(a)):
    #     temp.append(0)
    # #temp = np.zeros(len(a))
    # idx = len(a)
    # for i in range(len(a)):
    #     d = d % len(a) if d > len(a) else d
    #     if i < idx -1:
    #         temp[idx-d+i] = int(a[i])
    #     elif i == idx - 1:
    #         temp[0] = a[i]

    d = d % len(a) if d > len(a) else d
    temp = a[d:]+ a[:d]

    return temp


d = 10
a = [41, 73, 89, 7, 10, 1, 59, 58, 84, 77, 77, 97, 58, 1, 86, 58, 26, 10, 86, 51]
res = rotLeft(a, d)
print(res)

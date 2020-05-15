import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):

    a = sorted(arr)
    min = a[0]+a[1]+a[2]+a[3]
    max = a[1]+a[2]+a[3]+a[4]
    print(str(min) + ' '+ str(max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

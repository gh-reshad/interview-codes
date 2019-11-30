import math
import re
import sys
import random
import numpy as np


def sockMerchant(n, ar):
    pair = 0
    count = 0
    i = n -1
    arr = []
    while i < n and i >= 0:
        for j in range(len(ar)):
            if ar[i] not in arr:
                if ar[i] == ar[j]:
                    count += 1
        
        if count%2 == 0:
                    pair = pair + count/2
                    arr.append(ar[i])
        
        if count%2 == 1:
            pair = pair + (count-1)/2
            arr.append(ar[i])
        
        if count == 0:
            pair = pair + 0
            arr.append(ar[i])
        
        i -= 1
        count = 0
    
    return pair




if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')6


    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)

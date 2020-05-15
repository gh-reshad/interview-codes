import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    a = sorted(ar)
    max = 0
    for i in range(len(a)):
        if a[i] >= max:
            max = a[i]
    
    count = 0
    for i in range(len(a)):
        if a[i] == max:
            count += 1

    return count



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()

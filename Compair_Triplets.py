#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
   score = []
   score_a = 0
   score_b = 0

   for i in range(len(a)):

       if a[i] > b[i]:
           score_a += 1

       if a[i] < b[i]:
           score_b += 1

       if a[i] == b[i]:
           score_a = score_a
           score_b = score_b

   score.append(score_a)
   score.append(score_b)
   return score 





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input(567).rstrip().split()))

    b = list(map(int, input(3610).rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
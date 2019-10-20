import sys
import numpy as np


for lines in sys.stdin:
    input = lines[:-1]
    tokens = input.split(',')
    max = 0
    k = 0
    while k < len(tokens):
        if k+1 < len(tokens):
            diff = int(tokens[k+1]) - int(tokens[k])
            if diff >= max:
                max = diff
        k += 1

    print(max)

    # sum = 0
    # for i in range(len(str)):
    #     sum += int(str[i])

    # print(sum)
   


    
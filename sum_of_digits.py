import sys
import numpy as np


for lines in sys.stdin:
    input = lines
    tokens = input.split()
    #print(tokens)
    #print(type(tokens))
    str = np.asarray(tokens)
    #str = ''.join(x for x in tokens)
    print(str)
    max = 0
    arr = []
    k = 0
    while k < len(str):
        arr.append(str[k])
        k += 2
    
    print(arr)
 
   
   
    #     diff = int(str[i+1]) - int(str[i])
    #     if diff >= max:
    #         max = diff
    # print(max)
    # sum = 0
    # for i in range(len(str)):
    #     sum += int(str[i])

    # print(sum)
   


    
import numpy as np
import math
import os
import random
import sys

def superReducedString(s):
    arr = np.zeros(26,)
    reduced_arr = []
    for i in range(len(s)):
        var = ord(s[i]) - 97
        arr[var] += 1
        
 
    print(arr)
    for j in range(len(arr)):
        if arr[j] % 2 == 0:
            letter = chr(j + 97)
            if letter in s:
                pass
        elif arr[j] % 2 == 1:
            letter = chr(j + 97)
            if letter in s:
                reduced_arr.append(letter)                
                
    if len(reduced_arr) == 0:
        return 'empry string'
    else:
        return reduced_arr
    
    


    
if __name__ == '__main__':

    s = input().rstrip().split(' ')
    result = superReducedString(s)
    
    print(result)
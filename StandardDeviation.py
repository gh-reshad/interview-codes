import numpy as np
import math as m
import sys


def std(array, index):
    numbers = array
    idx = index
    sum = 0
    std = 0
    squaredError = 0
    
    #Find Mean
    for i in range(idx):
        sum += numbers[i]
    
    mean = sum / idx

    #Evaluate Standard Deviation
    for i in range(idx):
        squaredError = (numbers[i] - mean) ** 2
        std += squaredError
    
    
    return m.sqrt(std / idx)






if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = [int(token) for token in input().split()]
    res = std(arr, n)

    #print to 1 decimal scale
    print("{:.1f}".format(res))

import numpy as np
import math as m
import sys


def weightedMean(array, wieghts, index):
    length = index
    w = wieghts
    num = array
    sum = 0
    ws = 0
    
    for i in range(length):
        sum = sum + (w[i] * num[i])
        ws += w[i]
    
    return sum / ws






if __name__ == '__main__':

    n = int(sys.stdin.readline())
    arr = [int(token) for token in input().split()]
    w = [int(token) for token in input().split()]

    res = weightedMean(arr, w, n)

    #print to 1 decimal scale
    #print("{:.1f}".format(res))
    res = m.floor(res * 10)/10

    sys.stdout.write(str(res))
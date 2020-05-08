import numpy as np
import sys
import collections
import math as m


def MM(a, no):

    array = a
    index = no
    sum = 0
    #freq = collections.Counter(array)
    
    #Compute Mean
    for i in range(0, index):
        sum += int(array[i])
    
    Mean = sum / index

    #compute Median
    if index % 2 == 0:
        middle = m.floor(index/2)
        prev = m.floor(index/2) - 1
        Median = (int(array[middle]) + int(array[prev])) / 2
    
    else:
        middle = m.floor(index / 2)
        Median = array[middle]
    


    return Mean, Median

def mode(values: list) -> int:
	counters = dict()
	result = None
	for value in values:
		if value in counters:
			counters[value] += 1
		else:
			counters[value] = 1
		if (result is None) or (counters[value] > counters[result]):
			result = value
		elif (counters[value] == counters[result]) and (value < result):
			result = value

	return result





    



if __name__ == '__main__':
    #get the length of the arrat
    n = int(sys.stdin.readline())
    #get elements of array
    #arr = sys.stdin.readline().split(' ')
    arr = [int(token) for token in input().split()]
    

    mean, median = MM(arr, n)
    mode = mode(arr)

sys.stdout.write(mean)
sys.stdout.write(median)
sys.stdout.write(mode)
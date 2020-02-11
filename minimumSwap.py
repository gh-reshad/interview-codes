import numpy as np
import math as m
import random 

#ReadMe
#Brute Force Solution
#We find the smallest element in the array and exchange it with the element in the first poisition
#Then find the second smallest element in the array and swap it with the element in the second position
#Continue untill done. It does not find the min swap!!

#Efficient Solution:
#Look at each index and compare the index position with its value, if it's the same then move to the next index position
#If index position is not the same as element value then treat element value as index value for finding the next element
#If we comeback to the visited element then there exist a cycle, then count the size of the cycle, the number of swaps for 
#particular cycle will be size-1, do this for all the cylces and add them together

arr = [2, 3, 4, 1, 5]

def minSawps(arr):
     counter = 0
     temp = [0] * len(arr)

     for index, value in enumerate(arr):
          temp[value - 1] = index

     for i in range(len(arr)):
          if arr[i] != i+1:
               t = temp[i]
               arr[i], arr[t] = i+1, arr[i]
               temp[i], temp[arr[t] - 1] = i, t
               counter += 1
     
     return counter


res = minSawps(arr)
print(res)

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = 4
    if N % 2 == 1:
        print('Weird')
    
    if N % 2 == 0 and N in range(2,5):
        print('Not Wierd')
    
    if N % 2 == 0 and N in range(6,20):
        print('Weird')
    
    if N > 20:
        print('Not Weird')

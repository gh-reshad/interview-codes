import numpy as np
import sys
import math
import random
import os
import re



def staircase(num):
    n = num
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)




if __name__ == "__main__":
    n = int(input())

    staircase(n)
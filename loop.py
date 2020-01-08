import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    k = 1
    while k <= 10:
        result = n * k
        print('{0} x {1} = {2}'.format(str(n), str(k), str(result)))
        k += 1
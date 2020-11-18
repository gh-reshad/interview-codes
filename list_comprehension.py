import numpy as np
import sys

def listComprehenstion(a, b, c, num):

    list_comp = [[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a+b+c != num]
    

    return list_comp


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    result = listComprehenstion(x, y, z, n)
    print(result)
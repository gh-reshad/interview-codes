import numpy as np
import math
from collections import deque

def absoluteDiff(arr, num):
    n = len(arr)
    target = num
    q = deque()
    arr = np.sort(arr)
    for i in range(n-1):
        for j in range(len(arr)):
            q.append((i, j))
            if abs(arr[i] - arr[j]) != target:
                if abs(arr[i] - arr[i+1]) < target:
                    q.pop()
                else:
                    q.pop()
            else:
                return q


if __name__ == '__main__':
    arr = [5,8,10,14]
    target = 6
    res = absoluteDiff(arr, target)
    print(res)
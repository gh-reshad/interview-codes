import numpy as np
from collections import deque

def longestPalindromeSubstring(s):
    n = len(s)
    q = deque()

    for i in range(n):
        q.append((i,i))

    for i in range(n-1):
        if s[i] != s[i+1]:
            continue
        q.append((i, i+1))

    while q:
        i,j = q.popleft()
        i1 = i - 1
        j1 = j + 1
        if i1 < 0 or j1 > n-1:
            continue
        elif s[i1] != s[j1]:
            continue
        else:
            q.append((i1,j1))
    
    return s[i:j+1]

if __name__ == '__main__':
    s1 = str(input())
    res = longestPalindromeSubstring(s1)
    print(res)
import numpy as np

def sherlockAndAnagrams(arr):
    arr = list(arr)
    indexes = []
    for item in arr:
        idx = arr.index(item)
        list.remove()
        if item in arr:
            indexes[idx] = 1
    return indexes



if __name__ == '__main__':
    s = input()
    result = sherlockAndAnagrams(s)
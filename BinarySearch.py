import numpy as np

def BinarySearch(arr):
    low = 0
    high = arr.size() - 1
    array = []

    while low <= high:
        mid = (low + high) /2

        if array[mid] == value:
            return mid

        elif array[mid] < value:
            low = mid + 1

        elif array[mid] > value:
            high = mid - 1

    return -1





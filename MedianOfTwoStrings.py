import numpy as np

def findMedianSortedArray(num1, num2):
    arr1 = np.sort(num1)
    arr2 = np.sort(num2)

    arr = np.concatenate((arr1, arr2), axis=None)
    n = len(arr)
    

    if n%2 == 0:
        median = (arr[int(n/2)] + arr[int(n/2) + 1]) / 2
    
    else:
        median = arr[int(n/2)]
    
    return median


if __name__ == '__main__':
    num1 = [1,2]
    num2 = [3]
    num1 = np.array(num1)
    num2 = np.array(num2)
    res = findMedianSortedArray(num1, num2)
    print(res)
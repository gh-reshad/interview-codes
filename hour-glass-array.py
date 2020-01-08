import numpy as np


def hourglass(arr):

    sum = 0 
    max_hourglass = -63
    for i in range(1,5):
        for j in range(1,5):
            sum = 0
            sum += arr[i-1][j-1]
            sum += arr[i-1][j]
            sum += arr[i-1][j+1]
            sum += arr[i][j]
            sum += arr[i+1][j-1]
            sum += arr[i+1][j]
            sum += arr[i+1][j+1]

            if sum > max_hourglass:

                max_hourglass = sum
                
    return max_hourglass







if if __name__ == "__main__":
    
    arr = []
    
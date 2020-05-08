import math 
import sys



def median(array):
    n = len(array)
    #print('values =', array)
    if n%2 == 1:
        return sorted(array)[int((n+1)/2 -1)]

    else:
        return sum(sorted(array)[math.floor(n/2)-1: math.floor(n/2)+1]) / 2

def Quartiles(array):
    numbers = sorted(array)
    idx = len(numbers)

    Q2 = median(numbers)
    Q1 = median(numbers[:math.floor(idx/2)])
    if n%2 == 0:
        Q3 = median(numbers[math.floor(idx/2):])
    
    else:
        Q3 = median(numbers[(math.floor(idx/2))+1:])
    
    return Q1, Q2, Q3







if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = arr = [int(token) for token in input().split()]

    q1, q2, q3 = Quartiles(arr)

    print(int(q1),'\n',int(q2),'\n',int(q3))

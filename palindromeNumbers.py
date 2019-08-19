import numpy as np
import math as m

def is_palindromic(x):
    
    if x is not None:
        x = x.__str__()
        last = len(x) - 1
        if x[0] == x[last]:
            return True
        else:
            return False
    else:
        print('empty variable')

number = None
output = is_palindromic(number)
print(output)
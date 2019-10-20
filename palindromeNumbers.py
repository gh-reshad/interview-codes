import numpy as np
import math as m

def is_palindromic(x):
    
    if x is not None:
        x = x.__str__()
        y = np.zeros((len(x)))
        last = len(x) - 1
        idx = len(x)
        if x[0] == x[last]:
            for i in range(len(x)):
                y[i] = x[(idx-1) - i]
            return y
        else:
            return False
        
    else:
        print('empty variable')

number =  121
# is_palindromic(number)
output = is_palindromic(number)
print(output)
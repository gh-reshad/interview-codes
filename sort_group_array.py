import numpy as np

array = [0, 2, 3, 4, 5, 7, 8, 10]
array = sorted(array)

g = []
gr = []
idx = 0

while idx < len(array):

    first = array[idx]
    if first+1 in array:
        g.append(array[idx])
        g.append(array[idx+1])
        array = array[idx+2:]
        idx = 0
    else:
        gr.append(array[idx])
        array = array[idx+1:]
        idx = 0
    
print(g)
print(gr)

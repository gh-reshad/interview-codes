import sys


for lines in sys.stdin:
    input = lines
    tokens = input.split()
    print(tokens)
    str = ''.join(x for x in tokens)
    print(str)
    max = 0
    arr = []
    for i in range(len(str)):
        arr.append(str[i])

    print(arr)
   
    #     diff = int(str[i+1]) - int(str[i])
    #     if diff >= max:
    #         max = diff
    # print(max)
    # sum = 0
    # for i in range(len(str)):
    #     sum += int(str[i])

    # print(sum)
   


    
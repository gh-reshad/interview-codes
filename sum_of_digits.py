import sys

for lines in sys.stdin:

    input = lines
    tokens = input.split()
    str = ''.join(x for x in tokens)
    a = int(str[0])
    b = int(str[1])
    print('\n', a+b)

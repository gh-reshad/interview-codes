import numpy as np



def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


string = 'malayalam'
string1 = 'ababab'
result = isPalindrome(string)
print(result)
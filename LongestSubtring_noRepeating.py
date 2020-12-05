import numpy as np

def lenghtOfLongestSubstring(s):
    left = 0
    maxSubstringLength = 0
    charSet = set()
    
    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1

        charSet.add(s[right])
        maxSubstringLength = max(maxSubstringLength, right - left + 1)

    return maxSubstringLength



if __name__ == '__main__':
    s1 = str(input())
    res = lenghtOfLongestSubstring(s1)
    print(res)
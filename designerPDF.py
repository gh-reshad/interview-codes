import numpy as np
import sys
import os
import math
import re


def designerPDFViewer(h, word):
    maxi = 0
    for i in range(len(word)):
        if (maxi < h[ord(word[i]) - 97]):
            maxi = h[ord(word[i]) - 97]
        
    return maxi*len(word)




if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()
    result = designerPDFViewer(h, word)
    print(result)
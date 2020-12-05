###First Approach
from collections import Counter
from collections import defaultdict

# def ransom_note(magazine, ransom):
#     res = Counter(ransom) - Counter(magazine)
#     if res == {}:
#         return True
#     else:
#         return False

###Second Approach
def ransom_note(magazine, note):
    dicty = defaultdict(int)
    for word in magazine:
        dicty[word] += 1
    
    for word in note:
        if dicty[word] == 0:
            return 0
        dicty[word] -= 1
    
    return 1
        



if __name__ == '__main__':
    mn = input()
    mn = mn.split()
    m = int(mn[0])
    n = int(mn[1])

    magazine = input().rstrip().split()
    note = input().rstrip().split()

    ransom_note(magazine, note)




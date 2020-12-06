import numpy as np

##Assumption: the number that we are looking for should be in the range of our array

def firstMissingPositive(nums):
    if (nums == None or len(nums) == 0):
        return 1
    
    n = len(nums)
    containsOne = 0

    #Step 1 --->  turning negative and bigger than range (1, len(nums)) numbers to 1
    for i in range(n):
        if nums[i] == 1:
            containsOne = 1
        elif nums[i] < 0 or nums[i] > n:
            nums[i] = 1

    if containsOne == 0:
        return 1
    
    #Step 2 ---> using array items as indexes to turn non-negative numbers into negative
    for i in range(n):
        index = abs(nums[i]) - 1
        if nums[index] > 0 :
            nums[index] = -1 * nums[index]
    

    #Step 3 ---> Finding the first non-negative item and that will be our solution
    for i in range(n):
        if nums[i] > 0:
            return i+1
    
    #For edge case when we have no negative number in our array. example: [1,2,3]
    return n+1


if __name__ == '__main__':
    arr = [3,4,-1,1]
    res = firstMissingPositive(arr)
    print(res)
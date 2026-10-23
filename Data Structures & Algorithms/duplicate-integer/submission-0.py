class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
            if dic[i]>1:
                return True
        return False   
# create a dictionary
# loop through nums:
    #if there is no key then create one and count it
# loop thrrough the dictionary, if you find a value more than 1 then return True else False
'''
nums = [1, 2, 3, 3]
dic={}
Loop1-
iteration 1: nums = [1, 2, 3, 3]
    i=1
    dic = {1:1}

iteration 2: nums = [1, 2, 3, 3]
    i=2
    dic = {1:1, 2:1}

iteration 3: nums = [1, 2, 3, 3]
    i=3
    dic = {1:1, 2:1, 3:1}

iteration 4: nums = [1, 2, 3, 3]
    i=3
    dic = {1:1, 2:1, 3:2}

Loop2-
    dic = {1:1, 2:1, 3:2}
    value > 1:
        return True
    else:
        return False

TC: O(n+n) ~ O(n)
SC:          O(n)
'''
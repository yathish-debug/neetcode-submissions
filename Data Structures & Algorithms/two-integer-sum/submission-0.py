class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                return [dic[target-nums[i]], i]
            else:
                dic[nums[i]] = i

'''
create a dictionary
loop through the nums:
if target-i in dictonary:
    return i and as well as the index found in the dictionary 
else:
    add that to the dictionary
nums = [3,4,5,6], target = 7
dict = {}
iteration 0:
    i=3
    if target - 3 = 7-3=4 in the dict or not
    add present value tot the dictionary
    dict={3:0}

iteration 1:
    i=4
    if target - 4 = 7-4=3 in the dict or not. - yes
    return [dict[3],i]
    add present value tot the dictionary
    dict={0:3}
TC: O(n)
SC: O(n)
'''
        
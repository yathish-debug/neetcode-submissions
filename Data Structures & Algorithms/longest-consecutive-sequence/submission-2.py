class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxi=0
        for i in nums:

            if i-1 not in nums_set:
                cnt=1
                while i+1 in nums_set:
                    cnt+=1
                    i+=1
                maxi = max(maxi,cnt)
        return maxi
'''



'''
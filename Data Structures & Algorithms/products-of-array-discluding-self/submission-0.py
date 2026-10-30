class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        prod=1
        for i in range(len(nums)):
            pre.append(prod)
            prod = prod*nums[i]
        prod=1
        for k in range(len(nums)-1,-1,-1):
            suf.append(prod)
            prod = prod*nums[k]
        rev_suf = suf[::-1]
        output = [pre[i]*rev_suf[i] for i in range(len(pre))]
        return output
'''
pre=1
prod=1*1

pre=1,1
prod = 1*2

pre = 1,1,2
prod= 2*4

pre = 1,1,2,8
prod = 48

prod = 1

suf = 1
prod = prod*nums[i]

suf = 6,1
prod = 6*4

suf = 24,6,1
prod = 24*2

suf = 48,24,6,1
prod = 48*1
'''
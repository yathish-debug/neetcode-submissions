class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1
        while left<right:
            mid = (left+right)//2
            if nums[mid]>nums[right]: 
                left = mid+1
            else:
                right = mid
        return nums[left]
'''
nums = 3,4,5,6,1,2
left = 0
right = len(nums)-1
while left<=right:
    mid = (left+right)//2
    if nums[mid-1]>nums[mid]:
        return nums[mid]
    elif nums[mid-1]< nums[mid]:
        left = mid+1
    else:
        right = mid-1
return nums[left]
    
mid = 5
elif - left = 3
        ss = [6,1,2]

mid = 1
if - return 1


nums = [4,5,0,1,2,3]
nums = [4,5,6,7]

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            print(nums[left],nums[mid],nums[right],'mid')
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]: # check if left is sorted
                if nums[left]<=target<=nums[mid]: # check if target is between left to mid
                    right = mid-1
                else:
                    left = mid+1
            else:                   # check if right is sorted
                if nums[mid]<=target<=nums[right]: # # check if target is between mid to right
                    left = mid+1
                else:
                    right = mid-1
        return -1
'''
[3,4,5,6,1,2] target =1

mid = 5
is left sorted or right sorted:
    left is sorted:
        check is   left < target< mid
ss = [6,1,2]
mid = 1

ss= [1,2]
mid=1


nums = [3,5,6,0,1,2], target = 4
mid. =6
left or right?
    left
        left<target<mid




4,5,6,7,0,1,2 target =4
mid =7
 left:
    
ss = 0,1,2,
mid = 1
left:
right shift

ss = 0
left=right=mid=0



'''

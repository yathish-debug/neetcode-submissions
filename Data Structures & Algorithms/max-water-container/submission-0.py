class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 1
        right = len(heights)
        maxi_volume = 0
        heights.insert(0, -1)
        while left<right:
            width = right - left
            mini = min(heights[left], heights[right])
            volume = width*mini
            maxi_volume = max(maxi_volume, volume)
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maxi_volume
'''
loop through from both ends:
    maintain running max volume of water
    left = 
'''
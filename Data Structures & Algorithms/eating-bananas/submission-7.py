class Solution:
    def total_time(self, piles, k):
        total_time = 0
        for i in range(len(piles)):
            if piles[i]%k == 0:
                total_time+=(piles[i]//k)
            else:
                total_time+=(piles[i]//k)+1
        return total_time
    def rec(self, piles, low, high, target, ans):
        
        if low>high:
            return ans
        
        mid = (low+high)//2
        total_time = self.total_time(piles, mid)
        if total_time<=target:
            ans = mid
            return self.rec(piles,low, mid-1, target, ans)
        else:
            return self.rec(piles, mid+1, high, target, ans)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        return self.rec(piles, 1, max(piles), h, 1)
'''
# search space [1,2,3,4]
mid = 2


'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        c = float('inf')
        l = 0
        s = 0
        for r in range(len(nums)):
            s+= nums[r]
            while s >= target:
                c = min(c, r-l+1)
                s-= nums[l]
                l+=1
        return c if c < float('inf') else 0
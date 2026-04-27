class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        no = set(nums)
        l = 0
        for r in range(len(nums)):
            c = 1
            n = nums[r]
            if n-1 not in no:
                while n+1 in no:
                    c+=1
                    n+=1
            l = max(c,l)
        return l
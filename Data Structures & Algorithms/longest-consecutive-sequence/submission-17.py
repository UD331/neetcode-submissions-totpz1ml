class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        c = 0
        for i in range(len(nums)):
            num = nums[i]
            check = 1
            if num+1 not in n:
                while num-1 in n:
                    num-=1
                    check+=1
            c = max(c,check)
        return c

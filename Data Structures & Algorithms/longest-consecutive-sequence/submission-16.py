class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        c = 0
        for i in n:
            if i+1 not in n:
                check = 1
                while i-1 in n:
                    check+=1
                    i-=1
                c = max(check,c)
        return c

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = set(nums)
        c = 0 
        for i in range(len(nums)):
            count = 1
            nu = nums[i]
            if nu+1 not in nums:
                while nu-1 in n:
                    count+=1
                    nu-=1
            c = max(count, c)

        return c
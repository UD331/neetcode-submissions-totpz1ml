class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = len(nums)
        for i, n in enumerate(nums):
            s = s^i^n
        return s
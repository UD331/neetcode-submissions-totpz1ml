class Solution:
    def search(self, nums: List[int], target: int) -> int:
        u = len(nums) - 1
        l = 0
        while(l<=u):
            m = l + ((u - l) // 2)
            if target < nums[m]:
                u = m - 1
            elif target > nums[m]:
                l = m +1
            else:
                return m
        return -1   
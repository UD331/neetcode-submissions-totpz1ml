class Solution:
    def search(self, nums: List[int], target: int) -> int:
        u = len(nums) - 1
        l = 0
        while (l<=u):
            m = (l+u)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                u = m-1
            else:
                l = m +1
            
        return -1
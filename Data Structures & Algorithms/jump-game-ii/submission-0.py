class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        pos = nums[0]
        c = 0
        while c < len(nums)-1:
            pos = max(nums[c:c+pos])
            count += 1
            c = c+ pos
        return count
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pr, zero = 1, 0
        for n in nums:
            if n != 0:
                pr *=n
            else:
                zero+=1
        if zero >1:
            return [0] * len(nums)
        r = [0] * len(nums)
        for i, c in enumerate(nums):
            if c == 0:
                r[i] = pr
            elif zero and c!= 0:
                r[i] = 0
            else:
                r[i] = pr//c
        return r
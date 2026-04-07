class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l = []
        i = 0
        while i < len(nums):
            j = i+1
            while(j<len(nums)):
                k = j+1
                while k < len(nums):
                    if (nums[i] + nums[j] + nums[k]) == 0:
                        t = [nums[i], nums[j], nums[k]]
                        t = sorted(t)
                        print(t)
                        if t not in l:
                            l.append(t)
                            break
                    k += 1
                j+=1
            i+= 1
        return l
                    
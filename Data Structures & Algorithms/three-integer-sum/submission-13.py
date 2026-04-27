class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lis = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j<k:
                s = nums[i]+nums[j]+nums[k]
                if s < 0:
                    j+=1
                elif s > 0:
                    k-=1
                else:
                    lis.append([nums[i], nums[j], nums[k]])
                    k-=1
                    j+=1
                    while j<len(nums) and nums[j] == nums[j-1]:
                        j+=1

        return lis
                    
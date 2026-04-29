class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            l = 1
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    l = max(l,1+dfs(j))
            dp[i] = l
            return l
        return max(dfs(i) for i in range(len(nums)))
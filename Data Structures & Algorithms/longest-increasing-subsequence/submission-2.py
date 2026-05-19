class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [-1]*len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            l = 1
            for j in range(i+1, len(nums)):
                if nums[i] <nums[j]:
                    l = max(l, 1+dfs(j))
            dp[i] = l
            return dp[i]

        return max(dfs(i) for i in range(len(nums)))
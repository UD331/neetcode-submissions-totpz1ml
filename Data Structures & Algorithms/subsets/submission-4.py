class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def dfs(n):
            if n >= len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[n])
            dfs(n+1)
            sub.pop()
            dfs(n+1)
        
        dfs(0)
        return res
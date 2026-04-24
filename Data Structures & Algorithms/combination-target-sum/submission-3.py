class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, s, sub):
            if s == target:
                res.append(sub.copy())
                return
            if i >= len(nums) or s>target:
                return
            sub.append(nums[i])
            dfs(i,s+nums[i],sub)
            sub.pop()
            dfs(i+1,s,sub)
        
        dfs(0,0, [])
        return res
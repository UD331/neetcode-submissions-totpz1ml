class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        sub = []
        def dfs(i):
            if i>=len(nums):
                r.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
            return
        dfs(0)
        return r
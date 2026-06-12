class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        m = 0
        while l < r:
            if height[l] < height[r]:
                m = max(m,height[l]*(r-l))
                l+=1
            else:
                m = max(m,height[r]*(r-l))
                r-=1
        return m

            
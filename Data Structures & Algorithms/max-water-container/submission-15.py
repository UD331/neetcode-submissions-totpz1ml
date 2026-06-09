class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = 0
        while l < r:
            if heights[l] < heights[r]:
                m = max(m, heights[l]*(r-l))
                l+=1
            else:
                m = max(m, heights[r]*(r-l))
                r-=1
        return m

            
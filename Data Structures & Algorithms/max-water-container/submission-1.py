class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = 0
        while l < r:
            temp = min(heights[l], heights[r]) * (r-l)
            m = max(m, temp)
            if (heights[l] < heights[r]):
                l = l+1
            else:
                r = r-1
        return m
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = 0
        while l < r:
            lower = min(heights[l], heights[r])
            temp = (r-l) * lower
            m = max(m, temp)
            if lower == heights[l]:
                l+= 1
            else:
                r-=1
        return m
            
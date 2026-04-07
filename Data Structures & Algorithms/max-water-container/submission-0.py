class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1 
        m = 0
        while l <r:
            water = min(heights[l], heights[r]) * (r-l)
            m  = max(m, water)
            if heights[l] > heights[r]:
                r -=1
            else:
                l+=1
        return m
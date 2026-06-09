class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, m = 0, len(height)-1, 0
        lm, rm = height[l], height[r]
        while l < r:
            if height[l] < height[r]:
                lm = max(lm, height[l])
                m+= lm- height[l]
                l+=1
            else:
                rm = max(rm, height[r])
                m+= rm- height[r]
                r-=1
        return m
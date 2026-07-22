class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, m = 0, len(height)-1, 0
        lm, rm = height[l], height[r]
        while l <r:
            if height[l] < height[r]:
                l+=1
                lm = max(height[l], lm)
                m+= lm - height[l]
            else:
                r-=1
                rm = max(height[r], rm)
                m+= rm - height[r]
        return m
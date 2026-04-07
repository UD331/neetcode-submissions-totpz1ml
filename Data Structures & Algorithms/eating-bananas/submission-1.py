class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        found = r
        while (l <= r):
            m = (l+r)//2
            s = 0
            for p in piles:
                s += math.ceil(float(p) / m)
            if s > h:
                l = m +1
            else:
                found = m
                r = m -1
        return found
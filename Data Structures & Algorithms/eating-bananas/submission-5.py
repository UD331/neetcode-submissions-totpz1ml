class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l<=r:
            m = (l+r)//2
            c = 0
            for p in piles:
                c+= math.ceil(p/m)
            if c<=h:
                k = min(k,m);
                r = m-1
            else:
                l=m+1
        return k;
class Solution:
    def withinDays(self, weights, m):
        d = 1
        s = 0
        for w in weights:
            s+=w
            if s > m:
                d+=1
                s = w
        return d
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        wt = r
        while l<=r:
            m = (r+l)//2
            d = self.withinDays(weights, m)
            print(f"{d}\t{m}")
            if d <= days:
                wt = min(wt, m)
                r = m-1
            else:
                l = m+1
        return wt

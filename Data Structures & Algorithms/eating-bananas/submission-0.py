class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        u = max(piles)
        l = 1
        mi = u
        while (l<=u):
            m = int((l+u)/2)
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile / m)
            if totalTime > h:
                l = m + 1
            else:
                u = m - 1
                if m < mi:
                    mi = m

        return mi 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        m = prices[0]
        for pr in prices:
            if pr < m:
                m = pr
            else:
                p = max(p,pr-m)
        return p
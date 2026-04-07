class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m = 0
        for i in range(len(prices)-1):
            t = prices[i+1:]
            print(t)
            ma = max(t)
            s = ma - prices[i]
            if s > m:
                m = s
        return m
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        res = 0
        for p in prices:
            if p<buy:
                buy = p
            elif p-buy>res:
                res = p -buy
        return res
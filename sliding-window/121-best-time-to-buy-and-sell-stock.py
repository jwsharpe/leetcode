class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        priceMax = 0
        while r < len(prices):
            if prices[r] - prices[l] < 0:
                l = r
            else:
                priceMax = max(priceMax, prices[r] - prices[l]) 
            r += 1
        return priceMax

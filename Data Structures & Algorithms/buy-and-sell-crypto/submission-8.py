class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        ans = 0
        for sell in prices:
            ans = max(ans, sell - min_buy)
            if sell < min_buy:
                min_buy = sell
        return ans
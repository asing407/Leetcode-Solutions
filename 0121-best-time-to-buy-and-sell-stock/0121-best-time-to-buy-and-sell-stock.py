class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1

        maxProfit = 0

        while sell < len(prices):
            currProfit = prices[sell] - prices[buy]
            if prices[buy] < prices[sell]:
                maxProfit = max(currProfit, maxProfit)
            else:
                buy = sell

            sell += 1

        return maxProfit




        
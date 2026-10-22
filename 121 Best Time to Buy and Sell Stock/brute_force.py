class Solution:
    def maxProfit(self, prices):
        profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                p = prices[j] - prices[i]
                if p > profit:
                    profit = p

        return profit

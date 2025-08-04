class Solution:
    def maxProfit(self, prices):
        profit = 0
        bought = prices[0]

        for p in prices[1:]:
            if p < bought:
                bought = p
            if profit < p-bought:
                profit = p - bought
        
        return profit
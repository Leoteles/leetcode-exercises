# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# 5% 5%
class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        previous_min_price = prices[0]
        for i in prices[1:]:
            if i - previous_min_price > max_profit:
                max_profit = i - previous_min_price
            previous_min_price = min(previous_min_price,i)
        return max_profit
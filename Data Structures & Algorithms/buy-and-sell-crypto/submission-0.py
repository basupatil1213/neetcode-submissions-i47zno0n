class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        profit = 0
        curr_profit = 0
        buy_price = prices[0]

        for sell_price in prices:
            if sell_price < buy_price:
                buy_price = sell_price
                curr_profit = 0
            curr_profit = (sell_price - buy_price)
            profit = max(profit, curr_profit)
        
        return profit
        
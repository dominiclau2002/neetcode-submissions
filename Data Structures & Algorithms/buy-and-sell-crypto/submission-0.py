class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buying_price = prices[0]
        max_profit = 0
        min_buying_price = prices[0]

        for i in range(len(prices)):
            current_price = prices[i]

            if current_price < min_buying_price: #if current price > buying price profit will be > max_profit
                min_buying_price = current_price
            
            profit =  current_price - min_buying_price 

            if profit > max_profit:
                max_profit = profit


        return (max_profit)

                




        
        
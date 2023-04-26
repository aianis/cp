class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #Dynamic Progamming: extention of devide and conquer
        #1. Check if the list is empy
        n = len(prices)

        if n == 0:
            return 0
        
        #2. set the min and max: min is the initial index and the max is set to 0 until we loop and update

        min_price = prices[0]
        max_profit = 0 

        #3. Loop through and update the prices
        for i in range(1, n):
            if prices[i]<min_price:
                min_price = prices[i]
            elif prices[i]-min_price>max_profit:
                max_profit = prices[i]-min_price
        return max_profit

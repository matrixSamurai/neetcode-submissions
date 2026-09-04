class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minArray = [0] * len(prices)
        minPrice = 10**100 # Assigning the very large number to the variable
        maxPrice = -1
        maxProfit = 0;

        for index, num in enumerate(prices):
            minArray[index] = min(minPrice, num)

        for i in range(len(prices)-1 , -1, -1):
            maxPrice =  max(maxPrice, prices[i])
            maxProfit = max(maxProfit, max(0, maxPrice - minArray[i]))

        return maxProfit


        



        
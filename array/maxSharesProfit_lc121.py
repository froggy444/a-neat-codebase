class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimumBuyPrice = float('inf')
        result = 0
        for price in prices:
            minimumBuyPrice = min(minimumBuyPrice, price)
            potentialProfit = price - minimumBuyPrice
            result = max(result, potentialProfit)
        return result  
    
#O(n) Time and O(1) Space
            
            
            
            
        
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        
        
        while left < right:
            mid = (left + right )//2
            
            if self.shippingValid(mid, weights, days):
                right = mid
            else:
                left = mid + 1
                
        return right
        
    def shippingValid(self, candidate, weights, days):
        currentWeight = 0
        daysTaken = 1
        
        for weight in weights:
            currentWeight += weight
            
            if currentWeight > candidate:
                daysTaken += 1
                currentWeight = weight 
                
        return daysTaken <= days

# nlogn time and O(1) Space 
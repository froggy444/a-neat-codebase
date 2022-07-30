class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        width = right - left
        currentMaxArea = 0
        
        while (left < right):
            width = right - left
            currentArea = min (height[left], height[right]) * width
           
            if currentArea > currentMaxArea:
                currentMaxArea = currentArea
            
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return currentMaxArea
           
            
       
        
        
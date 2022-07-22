class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashSet = set(nums)
        sumOfAllUniqueElements = 0
        sumOfAllElements = 0
        
        for num in hashSet:
            sumOfAllUniqueElements += num
        
        for num in nums:
            sumOfAllElements += num
        
        return 2*sumOfAllUniqueElements - sumOfAllElements
            
# O(n) Space and Time 
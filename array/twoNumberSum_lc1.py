def twoNumberSum(array, targetSum):
  # o(nlogn) time | o(1) space 
	array.sort()
	left = 0
	right = len(array) - 1
	
	while left < right:
		currentSum= array[left] + array[right]
		if currentSum == targetSum:
			return [array[left], array[right]]
		elif currentSum < targetSum:
			left += 1
		else:
			right -=1
		
	return[]

# O(n) Time & Space
def twoNumberSum(array, targetSum):
	hash_map = {}
    for i in range(len(array)):
        if array[i] in hash_map:
            return [i, hash_map[array[i]]]
        else:
            hash_map[targetSum - array[i]] = i
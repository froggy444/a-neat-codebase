def longestPalindromicSubstring(string):
	currentLongest = [0, 1]
	# slice string [0:1] we store only indices 
	for i in range (1, len(string)): # no need to start from zero as we know first letter is pallindrome as per initial condition
		odd = getLongestPallindromeFrom(string, i-1, i+1)
		print('odd:',odd)
		even = getLongestPallindromeFrom(string, i-1, i)
		print('even:',even)
		longest = max(odd, even, key = lambda x: x[1] - x[0])
		print('longest:',longest) 
		currentLongest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
		print('currentLongest:',currentLongest)
	return string[currentLongest[0]:currentLongest[1] + 1]

def getLongestPallindromeFrom(string, leftIdx, rightIdx):
	while leftIdx >= 0 and rightIdx < len(string):
		if string[leftIdx] != string[rightIdx]:
			break
		leftIdx -= 1
		rightIdx += 1
	return[leftIdx + 1, rightIdx - 1]
#o(n^2) Time || O(n) space
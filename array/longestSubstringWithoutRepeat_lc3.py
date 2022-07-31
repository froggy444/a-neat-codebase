class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest=0
        currentLongest = 0
        for idx, c in enumerate(s):
            
            while (c != s[idx + 1]):
                if(currentLongest > longest):
                longest = currentLongest
                right += 1
                currentLongest = right - left
            left += 1
            right +=1
        return longest
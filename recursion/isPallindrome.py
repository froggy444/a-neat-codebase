def isPallindrome(s):
    left = 0
    right= len(s)-1
    if (len(s) <= 1):
        return True
    print (s[right - 1])
    return s[left] == s[right] and isPallindrome(s[left + 1 : right - 1])

#O(n) - Time || Space
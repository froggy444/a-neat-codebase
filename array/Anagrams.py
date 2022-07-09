#Valid anagram and variation Group Anagrams 

def groupAnagrams(words):
    # approach - declare a hashmap, sort each word and then add sortedWord as key and value is [word] (list containing single element original word) - 1st iteration, 
    # nth iteration however if sortedword is in the hashmap then append the original word to the list of values for the key as sortedWord
    #finally return a list of all the lists (using values() on hashmap to access the values) 

    anagrams = {}
	for word in words: 
		sortedWord = "".join(sorted(word))
        
		if sortedWord in anagrams:
			anagrams[sortedWord].append(word) # comment 2
            
		else:
			anagrams[sortedWord] = [word]    # comment 1
       
	return list(anagrams.values())          # comment 3

#O(w + nlogn) - Time || O(wn) - Space
# w is the number of words and n is the length of th longest word

def checkAnagram1(s, t):
    return sorted(s) == sorted(t)
#O(nlogn) - Time || O(1) - Space

def checkAnagram2(s, t):
    #approach is declare to hashmaps with count of each char and then compare the counts, if the counts are equal strings are valid anagrams 
    if len(s) != len(t):
        return False
    countS, countT = {}, {}
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0) # get the value of count for key s[i] and if key does not exist, default value 0 will returned this avoid key doesn't exist exception
        countT[s[i]] = 1 + countT.get(t[i], 0)
    for c in countS:
        if countS[c] != countT[get(c, 0)]:
            return False
    return True 


# Question why is checkAnagram1 a bad answer in the interview ? My thoughts interviewer may ask to implement the sorting and also it does not communicate any approach 








      
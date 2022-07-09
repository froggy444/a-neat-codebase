# approach - we are returning if seqIdx( increment counter for items present in sequence and array) is equal to len of sequence and also have a break condition prior to this
# break if seqIdx becomes equal to len of sequence

def isValidSubsequence(array, sequence):
	seqIdx = 0 
	for value in array:
		if seqIdx == len(sequence):
			break
		if sequence[seqIdx] == value:
			seqIdx +=1
	return seqIdx == len(sequence)
    
#O(n) - Time and O(1) Space - where n is the number of elements in array
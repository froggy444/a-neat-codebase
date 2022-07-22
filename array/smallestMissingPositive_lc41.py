def smallestMissingPositive(nums):
    currentSmallestPositive = 1

    if nums is None or min(nums) > currentSmallestPositive:
        return 1
  
    for num in nums:
        if(num ==currentSmallestPositive):
            currentSmallestPositive += 1
    return currentSmallestPositive

#doubt - solution follows constraint although is inefficient for larger lists, if take hashset of nums does it count as extra space ?
1 -> n + 1 if numbers are there from 1 to n solution n + 1
check only for possible solutions 
eliminate the negatives 
eliminate the numbers that are greater than length of array 

[3,4,-1,0]  n^2 we don't want cannot search for range one by one 


#smallestMissingPositive([1,7,8,9,11,12])
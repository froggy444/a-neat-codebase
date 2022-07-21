def smallestMissingPositive(nums):
    currentSmallestPositive = 1

    if nums is None or min(nums) > currentSmallestPositive:
        return 1
    currentSmallestPositive = 1
    for num in nums:
        if(num ==currentSmallestPositive):
            currentSmallestPositive += 1
    return currentSmallestPositive

#doubt - solution follows constraint although is inefficient for larger lists, if take hashset of nums does it count as extra space ?

#smallestMissingPositive([7,8,9,11,12])
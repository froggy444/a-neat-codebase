#Sol1 - heap klogn tc / n sc

from matplotlib import collections


def topKFrequentElements(nums, k):
    result = []
    freq = collections.Counter(nums) #builds dictionary with keys as num and values as frequency
    for val, count in freq.items():
        if len(result) < k:
            heapq.heappush(result, (count, val))
        else 
            heapq.heappush(result, (count, val))
            heapq.heappop(result)
    return [ val for count, val in result]



#sol 2 bucket sort trick - O(n) TC, SC

def topKFrequentElements(nums, k):
    freq = collections.Counter(nums)
        result =[]
        freqMatrixByIndex = [[] for i in range(len(nums) + 1)] # this will store element on count as index this is a list, for indices that have no frquencies it will be empty list, we cannot really have this sort of funnctionality without using array of lists, as normal array cannot store anything as None or empty
        for val, count in freq.items():
            freqMatrixByIndex[count].append(val)
        for i in range(len(freqMatrixByIndex) -1, 0, -1): #reverse order first -1 is index of last element , upto zero so zero and last -1 because we are going reverse from last element
            for num in freqMatrixByIndex[i]:
                
                result.append(num)
                if len(result) == k:  #terminating condition as we only need the k most frequent
                    return result
    
    


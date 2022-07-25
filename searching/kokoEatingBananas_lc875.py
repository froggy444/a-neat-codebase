class Solution:
    def getComputedHours(self, k: int, piles: List[int], h: int) -> int:
        computedHours = 0
        for pile in piles:
            if(pile <= k):
                computedHours += 1
                print ('loop1:', computedHours)
            else:
                computedHours += math.ceil(pile/k)
                print ('loop2:', computedHours)
                print ('computedHours:', computedHours)
        return computedHours
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        s= Solution()
        eatingSpeed = [x for x in range(min(piles), max(piles) + 1 )]
        print(eatingSpeed)
        left = 0 
        right = len(eatingSpeed)
       # print(s.getComputedHours(1,piles,h))
        while (left <  right):
            mid = (left + right)//2
            print('mid:', mid)
            print('len of eatingSpeed',len(eatingSpeed))
            print('eatingSpeed[mid]:', eatingSpeed[mid])
            if s.getComputedHours(eatingSpeed[mid], piles, h) == h:
                return eatingSpeed[mid]

            elif s.getComputedHours(eatingSpeed[mid], piles, h) < h:
                right = mid - 1
                 
            else:
                left = mid + 1 


                ###############################################################
                class Solution:
    def getComputedHours(self, k: int, piles: List[int], h: int) -> int:
        computedHours = 0
        for pile in piles:
            if(pile <= k):
                #if pile == piles[-1] and pile ==k:
                    #break
                computedHours += 1
               # print ('loop1:', computedHours)
            else:
                computedHours += math.ceil(pile/k)
               # print ('loop2:', computedHours)
               # print ('computedHours:', computedHours)
        return computedHours
    

    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        s= Solution()
        
        #print(eatingSpeed)
        left = 1 
        right = max(piles)+ 1
       
       # print(s.getComputedHours(1,piles,h))
        while (left < right):
            mid = (left + right)//2
           # print('mid:', mid)
           # print('len of eatingSpeed',len(eatingSpeed))
           # print('eatingSpeed[mid]:', eatingSpeed[mid])
            if s.getComputedHours(mid, piles, h) <= h:
                #return eatingSpeed[mid]

            #elif s.getComputedHours(eatingSpeed[mid], piles, h) < h:
                right = mid
                
                 
            else:
                left = mid + 1 
        
    
        return left
        
        
        
            
    
    
    
        
        
        
            
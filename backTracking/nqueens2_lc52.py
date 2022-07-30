#approach recursive backtrack is row wise so we are going row - wise 
#cols , pos and neg diagonal set h kyu ki we go to next value of cols in loop within backtrack
 #if any of the value is already in these sets
 #rememeber dynamic part is per row thats why us row ka kaam hone k baad we need to remove the values for the row from set 
 #this is why after running the backtracking again hum values nikal de rahe h set mai se  

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set() # r + c
        negDiag = set() # r - c 
        
        res = 0
        def backTrack(r):
            if r == n:
                nonlocal res 
                res += 1
                return 
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backTrack(r + 1)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        backTrack(0)  # start from row zero and recurse with r + 1

        return res   # return the answer
                
                
        
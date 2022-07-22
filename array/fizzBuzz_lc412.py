class Solution:
  
    def fizzBuzzLogic(self, i):
        if (i%3==0 and i%5==0):
            return "FizzBuzz"
        if (i%5 == 0):
            return "Buzz"
        if (i%3 == 0):
            return "Fizz"
        else:
            return str(i)
    def fizzBuzz(self, n: int) -> List[str]:
        return list(map(self.fizzBuzzLogic, range(1, n+1)))
    
    #O(n) Time and O(1) Space
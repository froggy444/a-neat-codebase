class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+': lambda y, x: x + y, '-': lambda y, x: x - y, '*': lambda y, x: x * y, '/': lambda y, x: int(x/y)  # IIFE and JUMP table concept for lambda functions in python          
        }
        
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop())) # the stack.pop() basically are args y, x for the lambda jump table 
                
            else:
                stack.append(int (token))
        return stack[-1]
        
# O(n) Time, Space
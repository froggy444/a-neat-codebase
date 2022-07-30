class Solution:

    
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
       
        stack = []
        answer=[0] * len(temperatures)
        
        for idx, value in enumerate(temperatures):
            while (stack and value > temperatures[stack[-1]]):
                top = stack.pop()
                answer[top] = idx - top
                
                #stack.append([value, idx])
                 
            
            stack.append(idx)
           
           
        
        return answer

            
        
        
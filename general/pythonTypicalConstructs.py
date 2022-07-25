#this file show cases tricks in python to implement code efficiently

#reverse loop - last element to zero in reverse order 

for(i in range(nums)-1 , 0 , -1):
    print(nums[i])
    result.append(nums[i]) #  appended reverse of nums in result 

#dictionary iterate and access keys and values 
freq = {}
for value, count in freq.items():
    result.append(count)

#jump table
operators = {'+': lambda y, x: x + y, '-': lambda y, x: x - y, '*': lambda y, x: x * y, '/': lambda y, x: int(x/y)  # IIFE and JUMP table concept for lambda functions in python          
        }
#accessing jump table and performing the lambda operation on popped elements of a stack
        for token in tokens:
            if token in operators:
                stack.append(operators[token](stack.pop(), stack.pop())) # the stack.pop() basically are args y, x for the lambda jump table 


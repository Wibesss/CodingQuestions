
# Write a program to sort a stack such that the smallest items are on the top. 
# You can use an additional temporary stack, but you may not copy the elements into any other data structure. 
# The stack supports the following operations: push, pop, peek, and isEmpty.

def sortStack(stack : list):
    tmpStack = []
    
    while stack:
        tmp = stack.pop()
        
        while tmpStack and tmp < tmpStack[-1]:
            stack.append(tmpStack.pop())
        
        tmpStack.append(tmp)
        
    while tmpStack:
        stack.append(tmpStack.pop())
    
    return stack
    
    
print(sortStack([1,3,5,2]))
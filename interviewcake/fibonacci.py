#Recursive method - slower
def fib(n):
    # write the body of your function here
    if n < 0:
        return ('Index is negative. '
                'Index in Fibonacci series cannot be negative.')
        
    elif n in [0, 1]:
        return n
    
    return fib(n-1) + fib(n-2)
        

# run your function through some test cases here
# remember: debugging is half the battle!
print fib(0)
print fib(15)
print fib(-1)

#Greedy method
def fibber(n):
    # write the body of your function here
    if n < 0:
        return ('Index is negative. '
                'Index in Fibonacci series cannot be negative.')
        
    elif n in [0, 1]:
        return n
    
    prev_prev = 0
    prev = 1
    
    for i in xrange(n-1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return current
    
print fibber(0)
print fibber(50)
print fibber(3)

#Recursive method - slower
def fib(n):
    # Edge case
    if n < 0:
        return ('Index is negative. '
                'Index in Fibonacci series cannot be negative.')
    # Base case    
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
    # Edge case
    if n < 0:
        return ('Index is negative. '
                'Index in Fibonacci series cannot be negative.')
    # Base case   
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

#Last digit of a large fibonacci number

def lastdigitfib(n):
    # Edge case
    if n < 0:
        return ('Index is negative. '
                'Index in Fibonacci series cannot be negative.')
    # Base case    
    elif n in [0, 1]:
        return n
    
    prev_prev = 0
    prev = 1
    
    for i in xrange(n-1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return current % 10
    
print lastdigitfib(0)
print lastdigitfib(331)
print lastdigitfib(3)


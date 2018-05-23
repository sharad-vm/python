# Write a function for finding the index of the "rotation point" 
def find_rotation_point(arg):
    # write the body of your function here
    floor = 0
    ceiling = len(arg) - 1
    
    while floor < ceiling:
        
        guess = floor + ((ceiling - floor)/2)
        
        if arg[guess] >= arg[0]:
            floor = guess
        else:
            ceiling = guess
        
        if floor + 1 == ceiling:
            return ceiling


# Test cases
# Remember: debugging is half the battle!
words = ['k', 'v', 'a', 'b', 'c', 'd', 'e', 'g', 'i']
print find_rotation_point(words)

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
print find_rotation_point(words)

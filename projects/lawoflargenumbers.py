import numpy as np

#Gets the user input for sample size
samplesize = int(raw_input("Please provide the samplesize:"))

#Function to generate random variables, count and find the mean based on the sample size provided
def lln(samplesize):
    r = np.random.randn(samplesize)
    counter = 0
    for number in r:
        if number <= 1 and number >= -1:
            counter = counter + 1
    mean = counter/float(samplesize)
    print "Numbers between 1 SD: %s" %counter
    print "Mean numbers between 1 SD: %s" %mean

lln(samplesize)

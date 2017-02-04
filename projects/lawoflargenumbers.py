import numpy as np

samplesize = int(raw_input("Please provide the samplesize:"))
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

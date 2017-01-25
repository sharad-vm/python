#More variables
'''Uses format strings.
You embed variables inside a string by using specialized format sequences and then
putting the variables at the end with a special syntax that tells Python, "Hey, this is a format string.
Put these variables in there."'''
name = "Ruby"
age = 10
weight = 51 #in lbs
height = 24 #inches
eyes = "brown"
teeth = "white"
hair = "black"


#Printing
print "Let's talk about ", name
print "He's %d inches tall" % height
print "He's %d pounds heavy" % weight, "or", weight / 2.2, "kgs"
print "Actually, that's not too heavy"
print "He's got %s eyes and %s hair." % (eyes,hair)
print("His teeth are usually %s depending on the coffee") % teeth
print

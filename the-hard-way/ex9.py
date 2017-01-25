days = "Mon Tue Wed Thu Fri Sat Sun"
Jan = "January"
Feb = "February"
Mar = "March"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#months using %r
quarter1 = "%r\n%r\n%r" %(Jan,Feb,Mar)
print "Here are the days: ", days
print "Here are the months: ", months
print "Here is the 1st quarter: ", quarter1
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

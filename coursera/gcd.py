#Task. Given two integers 𝑎 and 𝑏, find their greatest common divisor.
#Input Format. The two integers 𝑎, 𝑏 are given in the same line separated by space.

#GCD
def GCD(m, n):
	#Edge case
	if m == 0 or n == 0:
		return "One of the integers is 0."

	if m >= n:
		div = n
		rem = m % div
	else:
	    div = m
	    rem = n % div
	    m = n
	while rem != 0:
		rem = m % div
		if rem == 0:
		    return div
		m = div
		div = rem 
        return div    
 

#Test cases
print GCD(14, 4)
print GCD(8, 4)
print GCD(18, 35)
print GCD(28851538, 1183019)

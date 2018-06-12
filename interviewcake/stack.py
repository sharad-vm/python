# uses python 2
# implement a stack
class stack():
	
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[-1]

# Test cases
integers = stack()

integers.push(4)

integers.push(7)

integers.push(9)

print integers.peek()

print integers.pop()

print integers.peek()

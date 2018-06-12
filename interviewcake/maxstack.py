# uses python 2
# implement a stack
class stack():
	
	def __init__(self):
		self.items = []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if not self.items:
			return None 

		return self.items.pop()

	def peek(self):
		if not self.items:
			return None 

		return self.items[-1]

class MaxStack:

	def __init__(self):
		self.integers = stack()
		self.maxintegers = stack()

	def push(self, item):
		self.integers.push(item)

		if self.maxintegers.peek() is None or item > self.maxintegers.peek():
			self.maxintegers.push(item)

	def pop(self):
		item = self.integers.pop()

		if item == self.maxintegers.peek():
			self.maxintegers.pop()

		return item

	def get_max(self):
		return self.maxintegers.peek()

# Test cases


MaxInt = MaxStack()

MaxInt.push(4)

MaxInt.push(7)

MaxInt.push(9)

MaxInt.pop()

print MaxInt.get_max()

class Stack:
	def __init__(self):
		self.top = -1
		self.stack = []

	def push(self, data):
		self.stack.append(data)
		self.top += 1

	def pop(self):
		if self.top > -1:
			self.top -= 1
			return self.stack.pop()
		else:
			print("lol")
			raise Exception("Popping from Empty stack")

	def peek(self):
		if self.top > -1:
			return self.stack[self.top]
		raise Exception("No element on stack")

mystack = Stack()
mystack.push(12)
mystack.push(13)
mystack.push(144)

print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
print(mystack.pop())
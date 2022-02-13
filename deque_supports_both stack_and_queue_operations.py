#Deque supports both stack and queue operations

class Dequeue:
	def __init__(self):
		self.items = []

	def __str__(self):
		return "Hi"

	def isEmpty(self):
		return self.items == []

	def addFront(self, element):
		self.items.append(element)

	def addRear(self, element):
		self.items.insert(0, element)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

print (Dequeue())
d = Dequeue()
d.addFront("B")
d.addRear("A")

d.addFront("C")
d.addFront("D")


print(d.items)

d.removeRear()

print(d.items)

d.removeFront()
print(d.items) 
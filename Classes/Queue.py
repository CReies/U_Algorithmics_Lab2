class Queue:
	def __init__(self) -> None:
		self.data = []

	def getData(self):
		return self.data
	
	def queue(self, value: int) -> None:
		self.data.append(value)
	
	def dequeue(self, quantity: int) -> None:
		self.data = self.data[:-quantity]

	def modify(self, value: int,) -> None:
		for i in range(len(self.data)):
			if self.data[i] == value: break
			else: 
				self.dequeue(1)
		
	
	def is_empty(self) -> bool:
		return self.data == []
	
	def print(self) -> None:
		print(self.data)


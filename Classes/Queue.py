class Queue:
	def __init__(self) -> None:
		self.data = []

	def getData(self):
		return self.data
	
	def queue(self, value: int) -> None:
		self.data.append(value)
	
	def dequeue(self, quantity: int) -> None:
		self.data = self.data[quantity:]

	def modify(self, value: int) -> None:
		if self.data[0] == value: return
		else: 
			self.dequeue(1)
			self.modify(value)
		
	
	def is_empty(self) -> bool:
		return self.data == []
	
	def print(self) -> None:
		print(self.data)


class Stack:
	def __init__(self) -> None:
		self.data = []

	def getData(self):
		return self.data

	def stack(self, value: int) -> None:
		self.data.append(value)
	
	def unstack(self, quantity: int) -> None:
		self.data = self.data[quantity:]

	def modify(self, value: int) -> None:
		for i in range(len(self.queue)):
			if self.data[-i-1] == value: break
			else: 
				self.unstack(1)
	
	def is_empty(self) -> bool:
		return self.data == []
	
	def print(self) -> None:
		print(self.data)
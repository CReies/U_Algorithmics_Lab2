class Stack:
	def __init__(self) -> None:
		self.data = []

	def getData(self):
		return self.data

	def stack(self, value: int) -> None:
		self.data.append(value)
	
	def unstack(self, quantity: int) -> None:
		self.data = self.data[:-quantity]

	def modify(self, value: int) -> None:
		if self.data[-1] == value: return
		else: 
			self.unstack(1)
			self.modify(value)
	
	def is_empty(self) -> bool:
		return self.data == []
	
	def print(self) -> None:
		print(self.data)
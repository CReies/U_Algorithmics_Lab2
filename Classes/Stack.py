class Stack:
	def __init__(self) -> None:
		self.stack = []

	def stack(self, value: int) -> None:
		self.stack.append(value)
	
	def unstack(self, quantity: int) -> None:
		self.stack = self.stack[:quantity]

	def modify(self, value: int) -> None:
		for i in range(len(self.queue)):
			if self.queue[-i-1] == value: break
			else: 
				self.unstack(1)
	
	def is_empty(self) -> bool:
		return self.stack == []
	
	def print(self) -> None:
		print(self.stack)
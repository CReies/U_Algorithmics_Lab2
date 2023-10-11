class Queue:
	def __init__(self) -> None:
		self.queue = []
	
	def queue(self, value: int) -> None:
		self.queue.append(value)
	
	def dequeue(self, quantity: int) -> None:
		self.queue = self.queue[quantity:]

	def modify(self, value: int,) -> None:
		for i in range(len(self.queue)):
			if self.queue[i] == value: break
			else: 
				self.dequeue(1)
		
	
	def is_empty(self) -> bool:
		return self.queue == []
	
	def print(self) -> None:
		print(self.queue)

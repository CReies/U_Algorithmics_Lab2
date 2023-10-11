class Queue:
	def __init__(self) -> None:
		self.queue = []
	
	def queue(value: int, self) -> None:
		self.queue.append(value)
	
	def dequeue(quantity: int, self) -> None:
		self.queue = self.queue[:quantity]
	
	def is_empty(self) -> bool:
		return self.queue == []
	
	def print(self) -> None:
		print(self.queue)

import random as rand

class plane:

	def __init__(self, start_pos):
		self.current_destination = start_pos
		self.path = []
		if(start_pos == "1"):
			self.path = ["A", "A'", "TAKE_OFF"]
		elif(start_pos == "2"):
			self.path = ["F", "E", "D", "C", "B", "A", "A'", "TAKE_OFF"]
		elif(start_pos == "SKY"):
			num = rand.randint(0, 3)
			if(num == 0):
				self.path = ["TAKE_OFF"]
			elif(num == 1):
				self.path = ["B", "1", "A", "A'", "TAKE_OFF"]
			elif(num == 2):
				self.path = ["C", "1", "A", "A'", "TAKE_OFF"]
			else:
				self.path = ["D", "E", "F", "2", "F", "E", "D", "C", "1", "A", "A'", "TAKE_OFF"]

	def next_destination(self):
		if len(self.path) == 0:
			self.current_destination = "TAKE_OFF"
			return
		self.current_destination = self.path[0]
		del self.path[0]

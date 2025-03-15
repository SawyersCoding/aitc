
class edge:
	def __init__(self, to, weight):
		self.to = to
		self.weight = weight

class node:	
	def __init__(self, name, outgoing_edges):
		self.name = name
		self.outgoing_edges = outgoing_edges

class moncton_airport:

	def __init__(self):
		self.nodes = []
		self.edges = []
		self.create_nodes()

	def create_nodes(self):
		self.nodes.append(node("1", [edge("A", 1)]))

		self.nodes.append(node("2", [edge("F", 1)]))

		self.nodes.append(node("A", [edge("ICE", 1), 
							   edge("A'", 1)]))
		
		self.nodes.append(node("A'", [edge("TAKE_OFF", 1)]))

		self.nodes.append(node("B", [edge("A", 1), 
							   edge("1", 1)]))
		
		self.nodes.append(node("C", [edge("A", 1), 
							   edge("1", 1)]))
		
		self.nodes.append(node("ICE", [edge("A'", 1)]))

		self.nodes.append(node("SKY", [edge("TAKE_OFF", 1),
								 edge("B", 1),
								 edge("C", 1),
								 edge("D", 1)]))
		
		self.nodes.append(node("D", [edge("C", 1),
							   edge("E", 1)]))

		self.nodes.append(node("E", [edge("D", 1),
							   edge("F", 1)]))
		
		self.nodes.append(node("F", [edge("2", 1),
							   edge("E", 1)]))


## Quick testing
# airport = moncton_airport()

# for node in airport.nodes:
# 	print(node.name)
# 	for edge in node.outgoing_edges:
# 		print("   ", edge.to, edge.weight)
# 	print()
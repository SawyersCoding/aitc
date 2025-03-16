import moncton_airport as ma

class plane_wrapper:

	def __init__(self, plane, node, edge, ticks):
		self.plane = plane
		self.node = node
		self.edge = edge
		self.ticks = ticks

class airport_manager:

	def __init__(self, airport, plane_wrappers, plane_spawn_rate):
		self.next_plane_id = 0
		self.airport = airport
		self.plane_spawn_rate = plane_spawn_rate
		self.ticks_since_last_spawn = 0
		self.planes = {} # plane_id, plan_wrapper

		for p in plane_wrappers:
			self.planes[self.next_plane_id] = p
			self.next_plane_id += 1

	def tick(self):
		self.ticks_since_last_spawn += 1

		if self.ticks_since_last_spawn == self.plane_spawn_rate:
			self.ticks_since_last_spawn = 0
			self.spawn_plane()

		for p in self.planes.values():
			# Skip planes that have taken off
			if(p.node == "TAKE_OFF"):
				continue

			# update plane positions
			p.ticks += 1
			# Check if a new destination has been reached
			if p.ticks == p.edge.weight:
				p.node = self.airport.nodes[p.edge.to]
				p.ticks = 0
				p.plane.next_destination()

				for edge in p.node.outgoing_edges:
					if edge.to == p.plane.next_destination:
						p.edge = edge
						break

	def next_postion(self, plane_id):
		return self.planes[plane_id].edge.to

	def node_clear(self, plane_id, next_position):
		for p in self.planes.values():
			if p.node == next_position and p.ticks == 0:
				return False
		return True

	def is_plane_between(self, node_from, node_to, plane_id):
		for p in self.planes.values():
			if p.node == node_from and p.edge.to == node_to:
				return True
		return False

	def ticks_between(self, node_from, node_to):
		tick_list = []
		for p in self.planes.values():
			if p.node == node_from and p.edge.to == node_to:
				tick_list.append(p.ticks)
		return tick_list

	def spawn_plane(self):
		print("SPAWN A PLANE")
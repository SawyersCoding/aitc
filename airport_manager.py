import moncton_airport as ma
from plane import plane
import random as rand

class plane_wrapper:

	def __init__(self, plane, node, edge, ticks, name):
		self.plane = plane
		self.node = node
		self.edge = edge
		self.ticks = ticks
		self.name = name

class airport_manager:

	def __init__(self, airport, plane_wrappers, plane_spawn_rate):
		self.next_plane_id = 0
		self.airport = airport
		self.plane_spawn_rate = plane_spawn_rate
		self.ticks_since_last_spawn = 0
		self.planes = {} # plane_id, plan_wrapper

		self.airlines = ["AC", "UAC", "WJ", "SW"]

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
			if(p.node.name == "TAKE_OFF" or p.plane.skip):
				p.plane.skip = False
				continue


			# update plane positions
			p.ticks += 1
			# Check if waiting or a new destination has been reached
			if p.node.name == p.edge.to or p.ticks == p.edge.weight:
				p.node = self.airport.get_node[p.edge.to]
				p.ticks = 0
				p.plane.next_destination()

				for edge in p.node.outgoing_edges:
					if edge.to == p.plane.current_destination:
						p.edge = edge
						break

	def get_position(self, plane_id):
		return self.planes[plane_id].node.name

	def next_position(self, plane_id):
		return self.planes[plane_id].edge.to

	def node_clear(self, plane_id, next_position):
		for p in self.planes.values():
			if p.node.name == next_position and p.ticks == 0:
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

	def get_ticks(self, plane_id):
		return self.planes[plane_id].ticks
	
	def get_percent_complete(self, plane_id):
		return 100.0 * self.planes[plane_id].ticks / self.planes[plane_id].edge.weight

	def spawn_plane(self):
		# gen plane names for ids
		p_name = self.airlines[rand.randint(0, len(self.airlines) - 1)] + str(rand.randint(100, 999))

		p = plane("SKY")
		dest = None
		for e in self.airport.get_node["SKY"].outgoing_edges:
			if e.to == p.current_destination:
				dest = e
				break
		self.planes[self.next_plane_id] = plane_wrapper(p, self.airport.get_node["SKY"], dest, 0, p_name)
		self.next_plane_id += 1
		

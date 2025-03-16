
from ATC import weather
from ATC import ATC
from plane import plane
from airport_manager import airport_manager
from airport_manager import plane_wrapper
from moncton_airport import moncton_airport as ma
from moncton_airport import edge

def print_airport_state(air_manager):
	print("AIRPORT STATE:\n")
	for plane_id in air_manager.planes:
		print("\tPlane " + str(plane_id) + " is at " + air_manager.get_position(plane_id) + " and is going to " + air_manager.next_position(plane_id) + ". \n\t" + str(air_manager.get_percent_complete(plane_id)) + "% of the way there.\n\n")

def spawn_plane_wrapper(start_pos):
	p = plane(start_pos)
	dest = None
	for e in moncton.get_node[start_pos].outgoing_edges:
		if e.to == p.path[0]:
			dest = e
			break
	return plane_wrapper(p, moncton.get_node[start_pos], dest, 0)

w = weather()
w.set_weather(1, False)
moncton = ma()

# spawn planes
p_wrap = []
p_wrap.append(spawn_plane_wrapper("1"))
p_wrap.append(spawn_plane_wrapper("2"))
p_wrap.append(spawn_plane_wrapper("SKY"))

air_manager = airport_manager(moncton, p_wrap, 1000000)
atc = ATC(air_manager, w)

# Print state of airport
print_airport_state(air_manager)

# while(True):
for i in range(1):
	# Check decision tree

	# Decision tree should track responses already given
	# Decision tree should check reverse paths too
	# Refresh decision tree every tick
	for plane_id in air_manager.planes:
		response = atc.decision_tree(plane_id, air_manager.planes[plane_id].plane.current_destination)
		air_manager.planes[plane_id].plane.current_destination = response

	air_manager.tick()
	atc.clear_list()
	print_airport_state(air_manager)
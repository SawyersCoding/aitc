
from ATC import weather
from ATC import ATC
from plane import plane
from airport_manager import airport_manager
from airport_manager import plane_wrapper
from moncton_airport import moncton_airport as ma
from moncton_airport import edge
import random as rand

def print_airport_state(air_manager, i):
	print("AIRPORT STATE #" + str(i) + ":\n")
	print("\tPlane id\tPosition\tDestination\tPercent Complete\n")
	for plane_id in air_manager.planes:
		# print("\t{0:10}\t{0:10}\t{0:10}\t{0:10}".format(air_manager.planes[plane_id].name, air_manager.get_position(plane_id), air_manager.next_position(plane_id), str(air_manager.get_percent_complete(plane_id)) + "%"))
		print("\t" + air_manager.planes[plane_id].name + "\t\t" + air_manager.get_position(plane_id) + "\t\t" + air_manager.next_position(plane_id) + "\t\t" + str(air_manager.get_percent_complete(plane_id)) + "%")

def spawn_plane_wrapper(start_pos, airlines):
	p_name = airlines[rand.randint(0, len(airlines) - 1)] + str(rand.randint(100, 999))
	p = plane(start_pos)
	dest = None
	for e in moncton.get_node[start_pos].outgoing_edges:
		if e.to == p.current_destination:
			dest = e
			break
	return plane_wrapper(p, moncton.get_node[start_pos], dest, 0, p_name)


airlines = ["AC", "UAC", "WJ", "SW"]
w = weather()
w.set_weather(1, False)
moncton = ma()

# spawn planes
p_wrap = []
p_wrap.append(spawn_plane_wrapper("1", airlines))
p_wrap.append(spawn_plane_wrapper("1", airlines))
p_wrap.append(spawn_plane_wrapper("1", airlines))
p_wrap.append(spawn_plane_wrapper("1", airlines))
p_wrap.append(spawn_plane_wrapper("1", airlines))
p_wrap.append(spawn_plane_wrapper("2", airlines))
p_wrap.append(spawn_plane_wrapper("2", airlines))
# p_wrap.append(spawn_plane_wrapper("SKY", airlines))

air_manager = airport_manager(moncton, p_wrap, 5)
atc = ATC(air_manager, w)

# Print state of airport
i = 0
print_airport_state(air_manager, i)

while(True):
	a = input("Press enter to continue")
	i += 1
# for i in range(10):
	# Check decision tree

	# Decision tree should track responses already given
	# Decision tree should check reverse paths too
	# Refresh decision tree every tick
	for plane_id in air_manager.planes:
		response = atc.decision_tree(plane_id, air_manager.planes[plane_id].plane.current_destination)

		if(response != air_manager.planes[plane_id].plane.current_destination):
			air_manager.planes[plane_id].plane.path = [air_manager.planes[plane_id].plane.current_destination] + air_manager.planes[plane_id].plane.path
			air_manager.planes[plane_id].plane.current_destination = response

	air_manager.tick()
	atc.clear_list()
	print_airport_state(air_manager, i)
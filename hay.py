clear()
world_size = get_world_size()

def drone_action():
	global world_size

	for j in range(world_size):
		harvest()
		move(North)

while True:
	for i in range(world_size):	
		spawn_drone(drone_action)

		while num_drones() >= max_drones():
			pass

		move(East)

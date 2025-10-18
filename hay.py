# max_drones = 32
# world_size = 32

def drone_action():
	while True:
		harvest()
		move(North)
		

clear()
for i in range(max_drones() - 1):
	spawn_drone(drone_action)
	move(East)

drone_action()
	

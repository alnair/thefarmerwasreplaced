from utils import wait_for_all

clear()
set_world_size(max_drones() - 1)
world_size = get_world_size()

# Plant Step
def drone_action_plant_cacti():
	global world_size
	
	for i in range(world_size):
		if (get_ground_type() != Grounds.Soil):
			till()
		plant(Entities.Cactus)
		move(North)
	
def plant_cacti():
	global world_size
	drones = []
	
	for i in range(world_size):
		drones.append(spawn_drone(drone_action_plant_cacti))
		move(East)
	
	wait_for_all(drones)

# Sort Columns
def move_to_y_pos(y_target):
	y_curr = get_pos_y()
	moves_needed = y_target - y_curr
	if moves_needed > 0:
		dir = North
	else:
		dir = South
	for i in range(abs(moves_needed)):
		move(dir)

def drone_action_sort_col():
	global world_size

	for i in range(world_size):
		swapped = False
		for j in range(0, world_size - i - 1):
			move_to_y_pos(j)
			if measure() > measure(North):
				swap(North)
				swapped = True
		if not swapped:
			break

def sort_columns():
	global world_size
	drones = []
	
	for i in range(world_size):
		drones.append(spawn_drone(drone_action_sort_col))
		move(East)
	
	wait_for_all(drones)

# Sort Rows
def move_to_x_pos(x_target):
	x_curr = get_pos_x()
	moves_needed = x_target - x_curr
	if moves_needed > 0:
		dir = East
	else:
		dir = West
	for i in range(abs(moves_needed)):
		move(dir)

def drone_action_sort_row():
	global world_size

	for i in range(world_size):
		swapped = False
		for j in range(0, world_size - i - 1):
			move_to_x_pos(j)
			if measure() > measure(East):
				swap(East)
				swapped = True
		if not swapped:
			break
			
def sort_rows():
	global world_size
	drones = []
	
	for i in range(world_size):
		drones.append(spawn_drone(drone_action_sort_row))
		move(North)
	
	wait_for_all(drones)

while True:
	plant_cacti()
	sort_columns()
	sort_rows()
	harvest()

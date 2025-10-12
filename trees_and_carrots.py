clear()
set_world_size(max_drones() - 1)
world_size = get_world_size()

def plant_crop(x, y):
	if (x + y) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Carrot)
	
	if get_water() < 0.5:
			use_item(Items.Water)

def drone_action():	
	global world_size
	
	for i in range(world_size):
		if get_ground_type() != Grounds.Soil:
			till()
			plant_crop(get_pos_x(), i)

		if can_harvest():
			harvest()
			plant_crop(get_pos_x(), i)
			
		move(North)

while True:
	for i in range(world_size):
		spawn_drone(drone_action)
		
		while num_drones() >= max_drones():
			pass
			
		move(East)

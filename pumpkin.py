from utils import wait_for_all

clear()
set_world_size(max_drones() - 1)
world_size = get_world_size()
done = False

def check_pumpkin():
	left_value = measure()
	move(West)
	right_value = measure()
	move(East)
	return left_value == right_value

def plant_column():
	global world_size
	global done
	
	for i in range(world_size):
		if (get_entity_type() != Entities.Pumpkin):
			if (get_ground_type() != Grounds.Soil):
				till()
			plant(Entities.Pumpkin)
				
			if not done:
				while not can_harvest():
					if (get_entity_type() == Entities.Dead_Pumpkin):
						plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)
		move(North)

def plant_pumpkins():
	global world_size
	drones = []
	
	for i in range(world_size):
		drones.append(spawn_drone(plant_column))
		move(East)
	
	wait_for_all(drones)

while True:
	plant_pumpkins()
	done = False
	
	if check_pumpkin():
		harvest()
		done = True

width = 1280
height = 720
fps = 60
tilesize = 64
ground_width = 828
ground_height = 720
scale = 5
score = 0
highscore = 0
# inverted
spawn_rate = 20
object_rate = 75
wave = 1
count = 0
clock_back = 0
menu_open = False
highscore_page = False
level_page = False
menu_page = True
instructions_page = False

speed = 1

game_level = 0
map_created = False

phone = False

# Bools for Game Ending and Restarting
playerdeath = False
gameover = True

monster_data = {'squid': {'health': 100,'exp':100, 'damage':20,'image': 'squid.png', 'speed': 3, 'attack_radius': 80},
	'raccoon': {'health': 300,'exp':250,'damage':40,'image': 'raccoon.png','speed': 3, 'attack_radius': 120},
	'spirit': {'health': 100,'exp':110,'damage':8,'image': 'fire.png', 'speed': 4, 'attack_radius': 60},
	'bamboo': {'health': 70,'exp':120,'damage':6,'image': 'bamboo.png', 'speed': 3, 'attack_radius': 50},

	'fire_spirit': {'health': 150,'exp':150, 'damage':20,'image': 'fire_spirit.png', 'speed': 3, 'attack_radius': 80},
	'spider': {'health': 100,'exp':180,'damage':9,'image': 'spider.png','speed': 4, 'attack_radius': 50},
	'zombie': {'health': 200,'exp':160,'damage':12,'image': 'zombie_gnome.png', 'speed': 3, 'attack_radius': 60},
	'troll': {'health': 450,'exp':350,'damage':60,'image': 'troll.png', 'speed': 3, 'attack_radius': 120},
	}



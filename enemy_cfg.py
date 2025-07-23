# This module defines the enemy behaviour
import game_cfg

enemy_width = 30
enemy_height = 30
enemy_speed = 100
default_enemy_rotation = 0
enemy_detection_radius = 200
enemy_detection_angle = 90
enemy_sprite = game_cfg.get_resource_path("Resources/Sprites/Enemy/EnemyPrototype.png")
particle_count = 10
enemy_patrol_distance_threshold = 5
# This module defines the enemy behaviour

import pygame
from EnemyCfg import enemy1_l1_cfg
import enemy_cfg
import game_cfg

class Enemy:
    def __init__(self, pos, cfg):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(enemy_cfg.enemy_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (enemy_cfg.enemy_width, enemy_cfg.enemy_height))
        self.rect = self.image.get_rect(center=self.pos)
        self.is_at_patrol_point = True
        self.is_patroling = False
        self.patrol_timer = 0.0
        self.patrol_index = 0
        self.cfg = cfg


    def handle_events(self, delta_time):
        pass


    def update(self, delta_time):
        if self.is_at_patrol_point:
            self.patrol_timer += delta_time
            if self.patrol_timer >= self.cfg.enemy_patrol_times[self.patrol_index]:
                self.is_at_patrol_point = False
                self.is_patroling = True
                self.patrol_timer = 0.0
                self.patrol_index += 1
        if self.is_patroling:
            direction = pygame.Vector2(self.cfg.enemy_patrol_positions[self.patrol_index] - self.pos).normalize()
            if direction.length() > 0:
                self.pos += direction * enemy_cfg.enemy_speed * delta_time
                self.rect.center = self.pos
                if self.pos.distance_to(self.cfg.enemy_patrol_positions[self.patrol_index]) < enemy_cfg.enemy_patrol_distance_threshold:
                    self.is_at_patrol_point = True
                    self.is_patroling = False
                    if self.patrol_index >= len(self.cfg.enemy_patrol_positions) - 1:
                        self.patrol_index = 0


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self, screen_width, screen_height):
        if (self.pos.x < 0 or self.pos.x > screen_width or
            self.pos.y < 0 or self.pos.y > screen_height):
            game_cfg.objects_to_remove.append(self)
    
    def defeated(self):
        game_cfg.objects_to_remove.append(self)
        #particles = game_cfg.create_particles(self.pos, enemy_cfg.particle_count)#game_cfg.objects_to_instace.extend(particles)

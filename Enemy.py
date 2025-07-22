# This module defines the enemy behaviour

import pygame
import enemy_cfg
import game_cfg

class Enemy:
    def __init__(self, pos, cfg):
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(enemy_cfg.enemy_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (enemy_cfg.enemy_width, enemy_cfg.enemy_height))
        self.rect = self.image.get_rect(center=self.pos)


    def handle_events(self, delta_time):
        pass


    def update(self, delta_time):
        pass


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self, screen_width, screen_height):
        if (self.pos.x < 0 or self.pos.x > screen_width or
            self.pos.y < 0 or self.pos.y > screen_height):
            game_cfg.objects_to_remove.append(self)
    
    def defeated(self):
        game_cfg.objects_to_remove.append(self)
        #particles = game_cfg.create_particles(self.pos, enemy_cfg.particle_count)#game_cfg.objects_to_instace.extend(particles)

# This module defines the bullet behaviour

import pygame
import bullet_cfg
import game_cfg

class Bullet:
    def __init__(self, pos, direction):
        self.pos = pygame.Vector2(pos)
        self.direction = pygame.Vector2(direction).normalize()
        self.image = pygame.image.load(bullet_cfg.bullet_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (bullet_cfg.bullet_width, bullet_cfg.bullet_height))
        self.rect = self.image.get_rect(center=self.pos)

    def handle_events(self, delta_time):
        pass

    def update(self, delta_time):
        # Move the bullet in the specified direction
        self.pos += self.direction * bullet_cfg.bullet_speed * delta_time
        self.rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_off_screen(self, screen_width, screen_height):
        if (self.pos.x < 0 or self.pos.x > screen_width or
            self.pos.y < 0 or self.pos.y > screen_height):
            game_cfg.objects_to_remove.append(self)

    def check_collision(self, other_rect):
        game_cfg.objects_to_remove.append(self)


# This module defines the echo behaviour

import pygame
import echo_cfg


class Echo(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.pos = pygame.Vector2(pos)
        self.image = pygame.image.load(echo_cfg.echo_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (echo_cfg.width, echo_cfg.height))
        self.rect = self.image.get_rect(center=self.pos)


    def handle_events(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    #def draw(self, screen):
        #screen.blit(self.image, self.rect)
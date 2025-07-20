# This module defines the echo behaviour

import pygame
import echo_cfg

class Echo:
    def __init__(self,pos):
        self.pos = pos
        self.width = echo_cfg.width
        self.height = echo_cfg.height

    def handle_events(self, delta_time):
        pass

    def update(self, delta_time):
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, echo_cfg.color, (self.pos.x, self.pos.y, self.width, self.height))

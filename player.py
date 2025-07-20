# This module defines the Player class, which represents a player in the game.


import pygame
import echo
import player_cfg
import game_cfg
import math

class Player:
    def __init__(self, pos):
        self.pos = pygame.Vector2(pos)
        self.rotation = player_cfg.default_rotation
        self.echo_object_spawned = False
        self.echo_obj = None

        self.image = pygame.image.load(player_cfg.player_sprite).convert_alpha()
        self.image = pygame.transform.scale(self.image, (player_cfg.width, player_cfg.height))
        self.rect = self.image.get_rect(center=self.pos)



    def handle_events(self, delta_time):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.pos.x -= player_cfg.speed * delta_time
        if keys[pygame.K_d]:
            self.pos.x += player_cfg.speed * delta_time
        if keys[pygame.K_w]:
            self.pos.y -= player_cfg.speed * delta_time
        if keys[pygame.K_s]:
            self.pos.y += player_cfg.speed * delta_time
        if keys[pygame.K_e]:
            self.spawn_echo()
        if keys[pygame.K_SPACE]:
            self.shoot_weapon()
        if keys[pygame.K_q]:
            self.teleport()
        

    def update(self, delta_time):
        #mouse_pos = pygame.mouse.get_pos()
        #direction_x = mouse_pos.x - self.pos.x
        #direction_y = mouse_pos.y - self.pos.y
        #angle_rad = math.atan2(direction_y, direction_x)
        #angle_deg = math.degrees(angle_rad)
        #self.rotation = angle_deg
        self.rect = self.image.get_rect(center=self.pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        #pygame.draw.rect(screen, player_cfg.color, (self.pos.x, self.pos.y, self.width, self.height))

    def spawn_echo(self):
        if self.echo_object_spawned and self.echo_obj :
            return
        self.echo_object_spawned = True
        self.echo_obj = echo.Echo(self.pos.copy())
        game_cfg.objects_to_instace.append(self.echo_obj)

    def shoot_weapon(self):
        pass

    def teleport(self):
        if not self.echo_obj:
            return
        self.pos.x = self.echo_obj.pos.x
        self.pos.y = self.echo_obj.pos.y
        game_cfg.objects_to_remove.append(self.echo_obj)
        self.echo_obj = None
        self.echo_object_spawned = False
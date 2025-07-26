# This module defines the Player class, which represents a player in the game.


import pygame
import echo
import player_cfg
import game_cfg
import math
import bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.pos = pygame.Vector2(pos)
        self.rotation = player_cfg.default_rotation
        self.echo_object_spawned = False
        self.echo_obj = None
        self.can_shoot = True
        self.shooting_timer = 0.0

        self.original_image = pygame.image.load(player_cfg.player_sprite).convert_alpha()
        self.original_image = pygame.transform.scale(self.original_image, (player_cfg.width, player_cfg.height))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=self.pos)
        game_cfg.player_object.add(self)



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

        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.pos.x, mouse_y - self.pos.y
        angle_rad = math.atan2(rel_y, rel_x)
        self.rotation = (math.degrees(angle_rad) + 90) % 360
        self.image = pygame.transform.rotate(self.original_image, -self.rotation)
        self.rect = self.image.get_rect(center=(int(self.pos.x), int(self.pos.y)))

        if not self.can_shoot:
            self.shooting_timer += delta_time
            if self.shooting_timer >= player_cfg.shooting_interval:
                self.can_shoot = True
                self.shooting_timer = 0.0



    #def draw(self, screen):
        #screen.blit(self.image_copy, self.rect)

    def spawn_echo(self):
        if self.echo_object_spawned and self.echo_obj :
            return
        self.echo_object_spawned = True
        self.echo_obj = echo.Echo(self.pos.copy())
        game_cfg.instanced_objects.add(self.echo_obj)

    def shoot_weapon(self):
        if not self.can_shoot:
            return
        game_cfg.instanced_objects.add(bullet.Bullet(self.pos.copy(), pygame.Vector2(pygame.mouse.get_pos()) - self.pos))
        self.can_shoot = False

    def teleport(self):
        if not self.echo_obj:
            return
        self.pos.x = self.echo_obj.pos.x
        self.pos.y = self.echo_obj.pos.y
        self.echo_obj.kill()
        self.echo_obj = None
        self.echo_object_spawned = False

    def defeated(self):
        self.kill()
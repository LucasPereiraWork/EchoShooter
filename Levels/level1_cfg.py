# Thismodule defines the configuration for level 1 of the game.

import game_cfg
import enemy
import EnemyCfg.enemy1_l1_cfg as enemy1_l1_cfg
import player
import pygame

class Level1Config:
    def __init__(self):
        self.level_name = "Level1"
        self.background_image = game_cfg.get_resource_path("Resources/Backgrounds/Level1Prototype.png")
        self.player_start_pos = (game_cfg.window_width / 2, game_cfg.window_height / 2)
        self.enemy_spawn_positions = [
            (100, 100),
            (400, 250),
            (700, 400),
            (300, 600),
            (500, 150),
            (800, 350),
            (200, 450),
            (600, 550),
            (900, 200),
            (400, 500)
        ]
        self.enemy_count = len(self.enemy_spawn_positions)
        self.level_music = game_cfg.get_resource_path("Resources/Music/768402__sorlandal__electro-radioeffect_145.aiff")

    def load_level(self):
        # Load the background image
        game_cfg.background_image = pygame.image.load(self.background_image)

        game_cfg.instanced_objects.add(player.Player(self.player_start_pos))
        
        # Load enemies at specified spawn positions
        for pos in self.enemy_spawn_positions:
            game_cfg.instanced_objects.add(enemy.Enemy(pos, enemy1_l1_cfg))
        
        # Load level music
        game_cfg.load_music(self.level_music)
        
        # Set level name
        game_cfg.level_name = self.level_name
# Thismodule defines the configuration for level 1 of the game.

import game_cfg

class Level1Config:
    def __init__(self):
        self.level_name = "Level 1"
        self.background_image = "assets/level1_background.png"
        self.player_start_pos = (game_cfg.window_width / 2, game_cfg.window_height / 2)
        self.enemy_spawn_positions = [
            (100, 100),
            (200, 150),
            (300, 200),
            (400, 250)
        ]
        self.enemy_count = len(self.enemy_spawn_positions)
        self.level_music = "assets/level1_music.mp3"

    def load_level(self):
        # Load the background image
        game_cfg.background_image = self.background_image
        
        # Set player start position
        game_cfg.player_start_pos = self.player_start_pos
        
        # Load enemies at specified spawn positions
        for pos in self.enemy_spawn_positions:
            enemy_instance = game_cfg.create_enemy(pos)
            game_cfg.instanced_objects.append(enemy_instance)
        
        # Load level music
        game_cfg.load_music(self.level_music)
        
        # Set level name
        game_cfg.current_level_name = self.level_name
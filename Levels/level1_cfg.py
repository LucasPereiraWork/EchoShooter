# Thismodule defines the configuration for level 1 of the game.

import game_cfg
import enemy
import enemy1_l1_cfg

class Level1Config:
    def __init__(self):
        self.level_name = "Level1"
        self.background_image = "Resources/Backgrounds/Level1Prototype.png"
        self.player_start_pos = (game_cfg.window_width / 2, game_cfg.window_height / 2)
        self.enemy_spawn_positions = [
            (100, 100),
        ]
        self.enemy_count = len(self.enemy_spawn_positions)
        self.level_music = "Resources/Music/Level1.mp3"

    def load_level(self):
        # Load the background image
        game_cfg.background_image = self.background_image
        
        # Load enemies at specified spawn positions
        for pos in self.enemy_spawn_positions:
            game_cfg.objects_to_instace.append(enemy.Enemy(pos, enemy1_l1_cfg.enemy_patrol_positions))
        
        # Load level music
        game_cfg.load_music(self.level_music)
        
        # Set level name
        game_cfg.current_level_name = self.level_name
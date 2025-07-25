# Echo Shooter Game

import pygame
import player
import game_cfg
import Levels.level1_cfg as level1_cfg

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Create the window
screen = pygame.display.set_mode((game_cfg.window_width, game_cfg.window_height))
pygame.display.set_caption(game_cfg.window_title)

# delta time
game_clock = pygame.time.Clock()
delta_time = 0

# Load level
level_instance = level1_cfg.Level1Config()
level_instance.load_level()

game_cfg.level_setup()

# Game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            #pygame.quit()

    game_cfg.handle_events(delta_time)

    # Update game state
    game_cfg.update(delta_time)

    # Update Render
    game_cfg.render(screen)

    # Cap the frame rate
    delta_time = game_clock.tick(game_cfg.game_framerate) / 1000.0

# Quit Pygame
pygame.quit()

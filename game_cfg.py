import pygame
import os
import sys

# Window settings
window_width = 1280
window_height = 720
window_title = "Echo Shooter"
# Game settings
game_framerate = 60 # Frames per second this is default

# Game Objects settings
level_name = ""
background_image = None
background_rect = None

#Game Objects lists
instanced_objects = pygame.sprite.Group()  # Group to hold all game objects that are currently active
player_object = pygame.sprite.GroupSingle()  # Group to hold the player object
enemy_objects = pygame.sprite.Group()  # Group to hold all enemy objects
player_bullet = pygame.sprite.Group()  # Group to hold player bullets
enemy_bullet = pygame.sprite.Group()  # Group to hold enemy bullets



def get_resource_path(relative_path):

    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".") # Fallback for development

    return os.path.join(base_path, relative_path)

def level_setup():
    global background_image
    global background_rect

    background_image = pygame.transform.scale(background_image, (window_width, window_height))
    background_rect = background_image.get_rect(center = (window_width / 2, window_height / 2))

#Game Event loop
def handle_events(delta_time):
    for gameobject in instanced_objects:
        gameobject.handle_events(delta_time)
    return True

#Game Update loop
def update(delta_time):
    #for gameobject in instanced_objects:
        #gameobject.update(delta_time)

    instanced_objects.update(delta_time)  # Update all active game objects

    bullet_enemy_collisions = pygame.sprite.groupcollide(player_bullet, enemy_objects, True, True)
    bullet_player_collisions = pygame.sprite.groupcollide(enemy_bullet, player_object, True, True)

    for bullet, enemies in bullet_enemy_collisions.items():
        for enemy in enemies:
            print(f"Bullet hit enemy: {enemy} at {enemy.rect.center}")

    for bullet, players in bullet_player_collisions.items():
        for player in players:
            print(f"Enemy bullet hit player: {player} at {player.rect.center}")

#Game Render loop
def render(screen):

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    
    screen.blit(background_image, background_rect)

    instanced_objects.draw(screen)  # Draw all active game objects

    # Update the display
    pygame.display.flip()

def load_music(music):
    if not music:
        return
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)

def play_sound(sound):
    if not sound:
        return
    pygame.mixer.Sound(sound).play()

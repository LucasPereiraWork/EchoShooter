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
instanced_objects = []  # List to hold game objects
objects_to_instace = []  # List to hold objects to be instantiated
objects_to_remove = []  # List to hold objects to be removed

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
    for gameobject in instanced_objects:
        gameobject.update(delta_time)

    # Add new objects to the game
    for obj in objects_to_instace:
        if obj not in instanced_objects:
            instanced_objects.append(obj)

    # Clear the instancing list
    objects_to_instace.clear()
    
    # Remove objects that are marked for removal
    for obj in objects_to_remove:
        if obj in instanced_objects:
            instanced_objects.remove(obj)
    
    # Clear the removal list
    objects_to_remove.clear()

#Game Render loop
def render(screen):

    # Clear the screen
    screen.fill((0, 0, 0))  # Black background

    
    screen.blit(background_image, background_rect)

    for gameobject in instanced_objects:
        gameobject.draw(screen)

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

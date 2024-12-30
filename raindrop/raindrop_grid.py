import pygame
import sys
import os
if not os.path.exists('images/raindrop.png'):
    print("Error: Raindrop image not found.")
    sys.exit()
from pygame.sprite import Sprite

class Raindrop_grid(Sprite):
    """A class to represent a single raindrop in the grid."""

    def __init__(self, rain_game, settings):
        """Initialize raindrop grid and its behaviour."""
        super().__init__()
        self.screen = rain_game.screen
        self.settings = settings

        # Load the raindrop image
        try:
            self.image = pygame.image.load('images/raindrop.png')
        except FileNotFoundError:
            print("Error: Raindrop image not found. Using a placeholder.")
            self.image = pygame.Surface((20, 20))
            self.image.fill((0, 0, 255))

        # Set the rect attribute for positioning
        self.rect = self.image.get_rect()
        
        # Start each raindrop near the top-left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the raindrop's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_raindrop(self):
        """Draw a raindrop on the screen."""
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Make the raindrop fall from top to bottom of the screen."""
        self.rect.y += (self.settings.raindrop_speed
                         * self.settings.raindrop_direction)
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y
        print(self.settings)
        print(f"Direction: {self.settings.raindrop_direction}, "
              f"Speed: {self.settings.raindrop_speed}")
        
        if self.rect.y % 100 ==0:
            print(f"Position: {self.rect.y}")


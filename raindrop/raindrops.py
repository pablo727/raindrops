import pygame
import sys
from raindrop_settings import Settings
from raindrop_grid import Raindrop_grid

class Raindrops():
    """Overall class to manage raindrops."""
    
    def __init__(self):
        """Initialize rain drops, and create resources."""
        pygame.init()
        self.debug = True  # Debug flag
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((800, 600))  # Initialize screen
        pygame.display.set_caption("Raindrops")
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.raindrops = pygame.sprite.Group()  # Group for all the raindrops
        self._create_group_raindrops()

        if self.debug:
            print(f"screen dimensions: {self.settings.screen_width}x"
                  f"{self.settings.screen_height}")
            print(f"Initial number of raindrops: {len(self.raindrops)}")
    
    def run_game(self):
        """Starts the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)
            self._update_raindrops()
    
    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    def _update_raindrops(self):
        """Update position of raindrops and get rid old raindrops."""
        # Update raindrop positions
        for raindrops in self.raindrops.sprites():
            raindrops.update()

        # Get rid of raindrops that have disappeared and create new ones
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top > self.settings.screen_height:
                self.raindrops.remove(raindrop)
                # Create a new raindrop at the top
                self._create_raindrop(raindrop.rect.x, 0)  # Recycle position

    def _create_group_raindrops(self):
        """Create a group of raindrops."""
        # Create a raindrop to get its dimensions    
        new_raindrop = Raindrop_grid(self, self.settings)  # Call Raindrop_grid 
        raindrop_width, raindrop_height = new_raindrop.rect.size

        # Calculate number of raindrops that fit horizontally and vertically
        available_space_x = self.settings.screen_width - raindrop_width
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        available_space_y = self.settings.screen_height - raindrop_height
        number_rows = available_space_y // (2 * raindrop_height)

        # Create the grid of raindrops
        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                x = raindrop_number * (2 * raindrop_width)
                y = row_number * (2 * raindrop_height)
                self._create_raindrop(x, y)
    
    def _create_raindrop(self, x, y):
        """Create a raindrop."""
        new_raindrop = Raindrop_grid(self, self.settings)
        new_raindrop.rect.x = x
        new_raindrop.rect.y = y
        self.raindrops.add(new_raindrop)
        if self.debug:
            print(f"Position x: {x}, Position y: {y}")
        
    def _update_screen(self):
        """Update images on the screen, and flip to new screen."""
        self.screen.fill(self.settings.bg_color)  # Screen with bg color
        for raindrop in self.raindrops.sprites():
            raindrop.draw_raindrop() 
        self.raindrops.draw(self.screen)  # Automatic blits all drops in group
        pygame.display.flip()  # Update the display

if __name__ == '__main__':
    rain_game = Raindrops()
    rain_game.run_game()
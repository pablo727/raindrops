class Settings():
    """A class to store all settings for Raindrop game."""

    def __init__(self):
        """Initialize game's settings."""

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 220) # Background color

        # Raindrop settings
        self.raindrop_speed = 4.0
        self.raindrop_direction = 1
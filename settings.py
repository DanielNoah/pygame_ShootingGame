class Settings():
    """A class to store all settings for Younggi Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Younggi settings
        self.younggi_speed_factor = 1
        self.fleet_drop_speed = 30
        # fleet_direction of 1 represents right; -1 represts left.
        self.fleet_direction = 1

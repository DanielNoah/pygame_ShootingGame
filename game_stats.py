class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, invasion_settings):
        """Initialize statistics."""
        self.invasion_settings = invasion_settings
        self.reset_stats() # I'll initialize most statistics in the method reset stats() instead of directly in __init__().

        # Start Younggi Invasion in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.invasion_settings.ship_limit
        self.score = 0
        self.level = 1



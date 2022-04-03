import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship """

    def __init__(self, invasion_settings, screen, ship):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, invasion_settings.bullet_width, invasion_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx ## 이 부분 누락하면 미사일이 비행기에서 나가지 않고 화면 최좌측(0,0)에서 발사됨.
        self.rect.top = ship.rect.  top

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        self.color = invasion_settings.bullet_color
        self.speed_factor = invasion_settings.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

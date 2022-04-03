import pygame
from pygame.sprite import Sprite

class Younggi(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, invasion_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Younggi, self).__init__()
        self.invasion_settings = invasion_settings
        self.screen = screen


        # Load the younggi image and set its rect attribute.
        self.image = pygame.image.load("images/Younggi.bmp")
        self.rect = self.image.get_rect()

        # Start each new younggi near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the younggi at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        # game_functions의 check_fleet_edges 함수에서 loop문 내의 if 제어문에서 화면 구석(edge)에 닿는지 여부를 체크하는
        # 함수로 화면에 닿는 것은 화면의 오른쪽 사각형 크기보다 younggi image의 사각형이 크거나 같거면 True를 리턴, 아니면(elif) younggi
        # image의 사각형 좌측이 0보다 작거나 같으면 True을 리턴함. 이후 game_function의 check_fleet_edges 함수의 if문의
        # younggi.check_edges() 논리값이 True로 제어가 되면 change_fleet_direction(invasion_settings, younggis)가 호출되고
        # if문 빠져나오고, 계속해서 aliens.sprites() loop문 내에 있으므로 alien.check_edges()를 제어한다.

    def update(self):
        """Move the younggi right."""
        self.x += (self.invasion_settings.younggi_speed_factor * self.invasion_settings.fleet_direction)
        # 만약 fleet_direction이 1이면, younggi의 현재 위치에서 더하기가 되어 오른쪽으로 가고,
        # -1이면 값은 younggis의 position에서 빼기가 되어 왼쪽으로 움직인다.

        self.rect.x = self.x





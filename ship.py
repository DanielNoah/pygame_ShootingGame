import pygame
from pygame.sprite import Sprite

class Ship(Sprite): # Ship 클래스에 Sprite 클래스를 상속함.

    def __init__(self, invasion_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__() # 상속 상위클래스(Sprite)의 속성을 호출하는 super() 메서드를 통해 __init__() 자바로 치면 생성자 호출. .
        self.screen = screen
        self.invasion_settings = invasion_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flags (움직임 기본값-정지)
        self.moving_right = False # ship 객체의 움직임을 감지하지 않을 때(False)를 기본값으로 둠
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # ship 객체의 움직임이 감지되면 아래와 같이 중심에 위치한 ship을 오른쪽으로 1.5씩 이동 <<Refactoring>>되어서 코드라인X
            # (invasion.py에tj ship_speed_factor 속성을 Ship 클래스의 형식 파라미터로 setting 모듈에 지정한 스피드값 가져옴.
            # 스피드값 세팅모듈에 일원화 => Refactoring)
            self.center += self.invasion_settings.ship_speed_factor

        # elif로 분기되지 않고 if 블록으로 제어를 하는 이유는 좌우 방향키를 동시에 눌렀을 때의 조건(->멈춤) 감지와 오른쪽으로
        # 움직이는 것을 우선순위으로 두지 않기 위함.(p252 가운데 참조).
        # Update rect object from self.center
        # if self.moving_left and self.rect.left < self.screen_rect.left: 화면 최좌측에 해당하는 left 속성은 없음. <<리펙터링>>
        if self.moving_left and self.rect.left > 0: # 그래서 만약 사각형(ship)의 좌측값이 0보다 크다는 조건하에 ship은 화면의 좌측
            self.center -= self.invasion_settings.ship_speed_factor # 으로 넘어가지 않을 거임.
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx

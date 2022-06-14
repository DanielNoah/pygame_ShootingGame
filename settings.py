class Settings():
    """A class to store all settings for Younggi Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 2

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Younggi settings
        self.fleet_drop_speed = 1

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the younggis point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.younggi_speed_factor = .2

        # fleet_direction of 1 represents right; -1 represts left.
        self.fleet_direction = 1

        # Scoring
        self.younggi_points = 50

    # 기본 세팅 게임 스피드에서 비행기, 미사일, 영기(fleet) 스피드를 기존 수치에서 배로(multiply) 증가시킴
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.bullet_width *= self.speedup_scale
        self.younggi_speed_factor *= self.speedup_scale

        # self.younggi_points = int(self.younggi_points * self.score_scale)
        # print(self.younggi_points)

        # 게임의 속도가 증가함 때(한 번의 스테이지를 클리어할 때) 또한 각 점수의 기록폭도 증가시킨다(기본점수 50에서 1.5씩 곱하여 증가)

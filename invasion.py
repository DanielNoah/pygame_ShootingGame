import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from younggi import Younggi
import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    invasion_settings = Settings() # <- invasion_settings 변수에 Settings() 클래스의 속성으로 접근하기위해 대입함(함수 주소값 참조)
    screen = pygame.display.set_mode(
        (invasion_settings.screen_width, invasion_settings.screen_height))
    pygame.display.set_caption("Younggi Invasion")

    # Make the Play button.
    play_button = Button(invasion_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(invasion_settings)
    sb = Scoreboard(invasion_settings, screen, stats)

    # Make a ship. 인스턴스 객체 생성(로컬 메모리(스택)가 아닌 외부 공유하기 위한 글로벌 메모리(힙)에 저장)
    ship = Ship(invasion_settings, screen)

    # Make a Group to store bullets in
    bullets = Group()
    younggis = Group()

    # Create the fleet of aliens.
    gf.create_fleet(invasion_settings, screen, ship, younggis)

     # Start the  main loop for the game
    while True: # the main loop of the game, which is a while loop(무조건 반복문) that calls functions as below.
                # 왜 무조건 반복문을 쓸까? 중간에 게임이 종료되면 또 실행해야하므로, 프로그램이 종료하지 않도록 하기 위해.
        gf.check_events(invasion_settings, screen, stats, sb, play_button, ship, younggis, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(invasion_settings, screen, stats, sb, ship, younggis, bullets)
            gf.update_younggis(invasion_settings, screen, stats, sb, ship, younggis, bullets)

        gf.update_screen(invasion_settings, screen, stats, sb, ship, younggis, bullets, play_button)

run_game()

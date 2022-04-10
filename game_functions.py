import sys
from time import sleep

import pygame
from bullet import Bullet
from younggi import Younggi

# Move the ship to the right or left when users press down left or right arrow keys.
# elif event.type == pygame.KEYDOWN: << Refactoring >>
def check_keydown_events(event, invasion_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True  # ship 파일의 init(초기)함수의 moving_right flag가 True이므로 오른쪽으로 계속 움직임.
    # elif 다음 조건 분기문으로 제어를 하는 까닭은 각각의 이벤트는 단 하나의 키로로 연결되도록 제어하기 위함(p253 상단 참조).
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True  # ship 파일의 init(초기)함수의 moving_right flag가 True이므로 오른쪽으로 계속 움직임.

    elif event.key == pygame.K_SPACE:
        fire_bullet(invasion_settings, screen, ship, bullets)

    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(invasion_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet.  """
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < invasion_settings.bullets_allowed:
        new_bullet = Bullet(invasion_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    """Respond to key release."""
    # elif event.type == pygame.KEYUP: << Refactoring >>
    if event.key == pygame.K_RIGHT:
    # Move the ship to the right
        ship.moving_right = False # ship 파일의 init(초기)함수의 moving_right flag(누를동안 \
    # 움직이는 속성)가 Flase이므로 정지함.
    elif event.key == pygame.K_LEFT:
    # Move the ship to the left
        ship.moving_left = False # ship 파일의 init(초기)함수의 moving_left flag가 Flase이므로 정지함.


def check_events(invasion_settings, screen, stats, sb, play_button, ship, younggis, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, invasion_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(invasion_settings, screen, stats, sb, play_button, ship, younggis, \
                              bullets, mouse_x, mouse_y)

def check_play_button(invasion_settings, screen, stats, sb, play_button, ship, younggis, bullets, \
                      mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: #논리 연산자 and를 써서 화면 가운데 클릭과 \
        # 동시에 게임진행중이지 '아닌(not)' 상태에서만 재시작
        # Reset the game statistics.
        invasion_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False) #게임 시작 이후 마우스 커서 안보이게함.

        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of younggis and bullets.
        younggis.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(invasion_settings, screen, ship, younggis)
        ship.center_ship()

def update_screen(invasion_settings, screen, stats, sb, ship, younggis, bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(invasion_settings.bg_color)
    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    younggis.draw(screen)

    # Draw the score info.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()    

def update_bullets(invasion_settings, screen, stats, sb, ship, younggis, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet position.
    bullets.update()

    # Get rid of bullets that have disappered.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_younggi_collisions(invasion_settings, screen,stats, sb, ship, younggis, bullets)

def check_bullet_younggi_collisions(invasion_settings, screen, stats,sb, ship, younggis, bullets):
    """Resopond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    # Check for any bullets that have hit younggis.
    # If so, get rid of the bullet and the younggi.
    collisions = pygame.sprite.groupcollide(bullets, younggis, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += invasion_settings.younggi_points * len(younggis)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(younggis) == 0:  # younggis에 변수로 지정한 pygame.sprite의 group()
                            # 메서드의 길이가 0이라는 뜻은 the group younggis가
                            # 빈값(empty)이라는 뜻으로 기존의 미사일을 없애고, 새 전함(fleet)을 생성함.
                            # Destory existing bullets and create new fleet.
        # If the entire fleet is destroyed, start a new level.
        bullets.empty()
        invasion_settings.increase_speed()

        # Increase level. 스테이지 클리어 하면, 다음 스테이지(1 증가한) 값( prep_level() ) 호출해서 새로운 스테이지/
                            # 스코어 하단에 표시
        stats.level += 1
        sb.prep_level()

        create_fleet(invasion_settings, screen, ship, younggis)

def get_number_younggis_x(invasion_settings, younggi_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = invasion_settings.screen_width - 2 * younggi_width
    number_younggi_x = int(available_space_x / (2 * younggi_width))
    return number_younggi_x

def get_number_rows(invasion_settings, ship_height, younggi_height):
    """Determine the number of rows of younggis that fit on the screen."""
    available_space_y = (invasion_settings.screen_height - (3 * younggi_height)- ship_height)
    number_rows = int(available_space_y / (2 * younggi_height))
    return number_rows

def create_younggi(invasion_settings, screen, younggis, younggi_number, row_number):
    """Create Younggi and place him in the row."""
    younggi = Younggi(invasion_settings, screen)
    younggi_width = younggi.rect.width
    younggi.x = younggi_width + 2 * younggi_width * younggi_number
    younggi.rect.x = younggi.x
    younggi.rect.y = younggi.rect.height + 2 * younggi.rect.height * row_number
    younggis.add(younggi)

def create_fleet(invasion_settings, screen, ship, younggis):
    """Create a full fleet of aliens."""
    # Create an younggi and find the number of younggis in a row
    # Spacing between each younggi is equal to one younggi width.
    younggi = Younggi(invasion_settings, screen)
    number_younggis_x = get_number_younggis_x(invasion_settings, younggi.rect.width)
    number_rows = get_number_rows(invasion_settings, ship.rect.height, younggi.rect.height)

    # Create the fleet of younggi
    for row_number in range(number_rows):
        for younggi_number in range(number_younggis_x):
            create_younggi(invasion_settings, screen, younggis,younggi_number, row_number)

def check_fleet_edges(invasion_settings, younggis):
    """Repond appropriately if any younggis ahve reached an edge."""
    for younggi in younggis.sprites():
        if younggi.check_edges():
            change_fleet_direction(invasion_settings, younggis)
            break
        # younggis(비행체)가 화면의 edge(구석)에 닿는지를 체크하는 함수로 닿으면\
        # change_fleet_direction 함수를 호출하고
        # loop문을 빠져나옴(break).

def change_fleet_direction(invasion_settings, younggis):
    """Drop the entire fleet and change the fleet's direction."""
    for younggi in younggis.sprites():
        younggi.rect.y += invasion_settings.fleet_drop_speed
    invasion_settings.fleet_direction *= -1
    # younggi image의 사각형이 invasion_settings.fleet_drop_speed값\
    # '3'(setting값)만큼 증가하면서 loop문 이후 fleet_direction
    # 현재값에 -1을 곱해서 값의 부호를 변환, 즉 방향이 전환됨(좌측에서 우측 혹은 우측에서 좌측)

def check_younggis_bottom(invasion_settings, screen, stats, sb, ship, younggis, bullets):
    """Check if any younggis have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for younggi in younggis.sprites():
        if younggi.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(invasion_settings, screen, stats, sb, ship, younggis, bullets)
            break

def update_younggis(invasion_settings, screen, stats, sb, ship, younggis, bullets):
    """
    Check if the fleet is at an edge,
        and then update the position of all younggis in the fleet.
    """
    check_fleet_edges(invasion_settings, younggis)
    younggis.update()
    # update_younggis 함수를 통해 구석에 닿는 younggis 전함(fleet)이 \
    # check_fleet_edges()를 호출시키는 여부를 결정함. 이 함수는
    # invasion_settings 형식 파라미터가 필요하고, invasion_settings에 \
    # 필요한 인자(Settings 클래스의 세팅값)를 패스하여
    # update_younggis() 함수를 호출함.

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, younggis):
        ship_hit(invasion_settings, screen, stats, sb, ship, younggis, bullets)
        # print("Ship hit!!!") <- 게임 죽었을때 테스트 출력

    # Look for younggis hitting the bottom of the screen.
    check_younggis_bottom(invasion_settings, screen, stats, sb, ship, younggis, bullets)

def ship_hit(invasion_settings, screen, stats, sb, ship, younggis, bullets):
    """Respond to ship being hit by younggi."""
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1

        # Update scoreboard.
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        younggis.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(invasion_settings, screen, ship, younggis)
        ship.center_ship()

        # Pause.
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

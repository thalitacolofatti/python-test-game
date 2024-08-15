import pygame
import random
import time

def initialize_game():
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Be aware!")
    clock = pygame.time.Clock()
    return screen, clock

def load_assets():
    player_img = pygame.image.load("assets/images/player.png").convert_alpha()
    enemy_img = pygame.image.load("assets/images/enemy.png").convert_alpha()
    cure_img = pygame.image.load("assets/images/cure.png").convert_alpha()
    attack_img = pygame.image.load("assets/images/attack.png").convert_alpha()
    return player_img, enemy_img, cure_img, attack_img

def draw_player(screen, player_img, player_rect):
    screen.blit(player_img, player_rect)

def draw_enemy(screen, enemy_img, enemy_rect):
    screen.blit(enemy_img, enemy_rect)

def draw_cure(screen, cure_img, cure_rect):
    screen.blit(cure_img, cure_rect)

def draw_attack(screen, attack_img, attack_rect):
    screen.blit(attack_img, attack_rect)

def update_enemy(enemy_rect):
    enemy_rect.y += 5
    if enemy_rect.y > 510:
        return False  
    return True

def check_collision(player_rect, enemy_rect):
    if player_rect.colliderect(enemy_rect):
        return True
    return False

def check_cure_collision(player_rect, cure_rect):
    if player_rect.colliderect(cure_rect):
        return True
    return False

def check_attack_collision(attack_rect, enemy_rect):
    if attack_rect.colliderect(enemy_rect):
        return True
    return False

def draw_info(screen, hp, time_left, kills):
    font = pygame.font.Font(None, 32)
    hp_text = font.render(f"HP: {hp}", True, (255, 255, 255))
    time_text = font.render(f"Time: {int(time_left)}", True, (255, 255, 255))
    kills_text = font.render(f"Kills: {kills}", True, (255, 255, 255))
    screen.blit(hp_text, (10, 10))
    screen.blit(time_text, (340, 10))
    screen.blit(kills_text, (680, 10))

def draw_message(screen, message):
    font = pygame.font.Font(None, 90)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000) 

def run_game(screen, clock):
    player_img, enemy_img, cure_img, attack_img = load_assets()
    player_rect = player_img.get_rect(center=(400, 500))
    attack_rect = attack_img.get_rect(center=(player_rect.centerx, player_rect.centery)) #top

    enemy_rect = None
    cure_rect = None

    hp = 20
    kills = 0
    attack_count = 0
    start_time = time.time()

    last_enemy_time = 0
    attacking = False

    running = True
    while running:
        time_left = 60 - (time.time() - start_time)
        if time_left <= 0 and hp > 0:
            draw_message(screen, "You Win!")
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left > 0:
            player_rect.x -= 5
        if keys[pygame.K_RIGHT] and player_rect.right < 800:
            player_rect.x += 5
        if keys[pygame.K_SPACE]:
            attacking = True
            attack_rect = attack_img.get_rect(center=(player_rect.centerx, player_rect.top))
            if enemy_rect and check_attack_collision(attack_rect, enemy_rect):
                kills += 1
                enemy_rect = None
                attack_count += 1
                if attack_count == 3:
                    cure_rect = cure_img.get_rect(center=(random.randint(0, 750), 510))
                    attack_count = 0

        current_time = pygame.time.get_ticks()
        if not enemy_rect and current_time - last_enemy_time > 1000:
            last_enemy_time = current_time
            enemy_rect = enemy_img.get_rect(topleft=(random.randint(0, 750), -50))

        if enemy_rect:
            if not update_enemy(enemy_rect):
                enemy_rect = None  

        if enemy_rect and check_collision(player_rect, enemy_rect):
            hp -= 1
            enemy_rect = None  
            if hp <= 0:
                draw_message(screen, "Game Over!")
                running = False

        if cure_rect and check_cure_collision(player_rect, cure_rect):
            hp += 1
            cure_rect = None

        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (50, 205, 50), pygame.Rect(0, 500, 800, 100))
        draw_player(screen, player_img, player_rect)
        if enemy_rect:
            draw_enemy(screen, enemy_img, enemy_rect)
        if cure_rect:
            draw_cure(screen, cure_img, cure_rect)
        draw_info(screen, hp, time_left, kills)
        if attacking:
            draw_attack(screen, attack_img, attack_rect)
            attacking = False

        pygame.display.flip()
        clock.tick(60)
import pygame

def draw_menu(screen, menu_items, selected_item):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    
    for index, item in enumerate(menu_items):
        color = (255, 255, 0) if index == selected_item else (255, 255, 255)
        text_surface = font.render(item, True, color)
        screen.blit(text_surface, (300, 200 + index * 60))
    
    pygame.display.flip()

def draw_text(screen, text, position, font, color=(255, 255, 255)):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)

def draw_button(screen, text, position, size, font):
    button_rect = pygame.Rect(position, size)
    pygame.draw.rect(screen, (255, 255, 0), button_rect)
    text_surface = font.render(text, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=button_rect.center)
    screen.blit(text_surface, text_rect)
    return button_rect

def show_help(screen, font):
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_text(screen, "HELP - Game Controls", (250, 50), font)
        draw_text(screen, "LEFT/RIGHT arrows: Moves the player", (200, 150), font)
        draw_text(screen, "SPACE: Attack", (200, 200), font)
        draw_text(screen, "ESC: Quit game", (200, 250), font)
        draw_text(screen, "Meat increase HP, Enemies decrease.", (200, 320), font)

        # Botão de voltar ao menu
        back_button = draw_button(screen, "Back", (300, 450), (200, 50), font)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    running = False


def menu_loop(screen, clock):
    menu_items = ["Start Game", "Help", "Quit"]
    selected_item = 0
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_item = (selected_item + 1) % len(menu_items)
                elif event.key == pygame.K_UP:
                    selected_item = (selected_item - 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    if selected_item == 0:
                        return "start_game"
                    elif selected_item == 1:
                        return "help"
                    elif selected_item == 2:
                        return "quit"
        
        draw_menu(screen, menu_items, selected_item)
        clock.tick(30)
import pygame
import sys
from game_functions import initialize_game, run_game
from menu_functions import menu_loop, show_help

def main():
    pygame.init()
    screen, clock = initialize_game()
    font = pygame.font.Font(None, 32)
    
    while True:
        menu_result = menu_loop(screen, clock)
        if menu_result == "start_game":
            run_game(screen, clock)
        elif menu_result == "help":
            show_help(screen, font)
        elif menu_result == "quit":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
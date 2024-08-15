# PyGame Project Test

## Description

This is a simple game created using the PyGame library. The objective of the game is to **dodge the falling enemies** while collecting health items to stay alive. The game features a menu with a help section that explains the controls.

## Features

- A simple menu (text-based).
- The game runs at 60 frames per second and updates the display accordingly.
- Custom-made functions for managing the game logic and user interface.
- A menu screen that includes a "Help" button, displaying the game controls and information.
- Enemies appear one at a time in random locations, challenging the player to dodge them.
- The player loses HP when hit by enemies. Health can be restored by collecting health items.
- A timer counts up to 60 seconds. If the player survives for 60 seconds, a "You Win" message is displayed. If the player's HP reaches zero, a "Game Over" message is shown.
- The player's HP and the timer are updated in real-time on the screen.
- After every three attacks, a health item appears, which the player can collect to restore HP.


## How to Play

- Start the game and navigate through the menu using the mouse.
- Click on "Help" to see the controls and game instructions.
- In the game, use the arrow keys to dodge falling enemies and the spacebar to attack.
- Survive for 60 seconds to win, or collect health items to prolong your survival.

## Installation

1. Ensure you have Python installed.
2. Install the required dependencies using:

    ```bash
    pip install pygame
    ```

## How to Run

1. Make sure you have Python and PyGame installed.
2. Clone or download the repository.
3. Run the game using:
    ```bash
    python main.py
    ```

## Controls

- LEFT/RIGHT: move the player left or right.
- SPACEBAR: attack.
- ESCAPE: exit the game.

## License

This project is licensed under the MIT License.

## Credits

I used art by [Pixel Frog](https://pixelfrog-assets.itch.io/tiny-swords)
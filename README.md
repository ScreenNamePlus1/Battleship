# Battleship Game

This is a command-line implementation of the classic Battleship game in Python.

## How to Play

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/ScreenNamePlus1/Battleship.git
    ```
2.  **Run the Game:**
    ```bash
    python Battleship.py
    ```
3.  **Ship Placement:**
    * Players take turns placing their ships on a 10x10 grid.
    * You'll be prompted to enter coordinates (e.g., `A5`) and an orientation (`H` for horizontal, `V` for vertical).
    * Ships cannot overlap or extend beyond the board's boundaries.
4.  **Taking Shots:**
    * Players take turns guessing the coordinates of the opponent's ships.
    * Enter coordinates (e.g., `B3`) to fire a shot.
    * `X` marks a hit, and `O` marks a miss.
5.  **Winning:**
    * The first player to sink all of the opponent's ships wins.

## Game Rules

* The game uses a standard 10x10 grid.
* The following ships are used:
    * Carrier (size 5)
    * Battleship (size 4)
    * Cruiser (size 3)
    * Submarine (size 3)
    * Destroyer (size 2)
* Ships can be placed horizontally or vertically.
* Ships cannot overlap.
* Players take turns firing shots.
* The game ends when one player has sunk all of the opponent's ships.

## Improvements

* Clear screen between turns.
* Display updated shot board after each shot.
* Improved coordinate and orientation input validation.
* Added more descriptive error messages.

## Future Improvements

* Add a function to check for sunk ships.
* Add random ship placement.
* Add game difficulty options.
* Add more robust error handling.
* Add clear screen functionality for better UI.

## Author

[ScreenNamePlus1]

MIT license

# Battleship2 Multiplayer over Wi-Fi ⚓️

Dive into the classic naval strategy game, Battleship, now with multiplayer action over Wi-Fi! Outsmart your opponent, sink their fleet, and claim victory on the high seas!

![Battleship Game Logo](path/to/battleship_logo.png)  *(Replace with your game logo image)*

## How to Play 🎮

1.  **Launch the Game:**
    * Open your terminal or command prompt.
    * Navigate to the directory containing `Battleship.py`.
    * Execute the game: `python Battleship.py`

2.  **Choose Your Role:**
    * The game prompts you: Server (S) or Client (C)?
    * **Server (S):** Hosts the game, providing the connection point.
    * **Client (C):** Joins the server's game.

    ![Server Client Selection](path/to/server_client_selection.png) *(Replace with an image showing server/client selection)*

3.  **Server Setup (If Applicable):**
    * The server displays its IP address and port.
    * The client needs this info to connect.

    ![Server IP Display](path/to/server_ip_display.png) *(Replace with an image of the server IP display)*

4.  **Client Connection (If Applicable):**
    * The client enters the server's IP address.

    ![Client IP Input](path/to/client_ip_input.png) *(Replace with an image of the client IP input)*

5.  **Ship Placement 🚢:**
    * Place your fleet on the 10x10 grid.
    * Ships: Carrier (5), Battleship (4), Cruiser (3), Submarine (3), Destroyer (2).
    * Enter coordinates (e.g., A5) and orientation (H/V).

    ![Ship Placement Example](path/to/ship_placement.png) *(Replace with a screenshot of ship placement)*

6.  **Engage in Combat 💥:**
    * Take turns firing shots by entering coordinates.
    * "Hit!" or "Miss!" feedback is provided.
    * Sink all enemy ships to win!

    ![Gameplay Screenshot](path/to/gameplay_screenshot.png) *(Replace with a gameplay screenshot)*

7.  **Victory! 🏆:**
    * The first player to sink all opponent ships wins.

    ![Victory Screen](path/to/victory_screen.png) *(Replace with a victory screen image)*

8. **Quitting**
    * entering "Q" at the coordinates prompt, will close the connection.

## Dependencies 📦

* Python 3.x (Standard libraries: `socket`, `json`, `os`)

## Running the Game 🚀

1.  Ensure both devices are on the same Wi-Fi network.
2.  Run `Battleship.py` on both devices.
3.  Choose server/client roles.
4.  Follow on-screen instructions.

## Notes 📝

* Firewall settings may need adjustment.
* Error handling for network and input errors included.
* Single-board display per player.
* JSON for data transfer over sockets.

## Future Enhancements 🛠️

* Graphical User Interface (GUI).
* Advanced error handling.
* Save/load game feature.
* Improved network robustness.
* Threading for connection management.

## Image Creation Tips:

1.  **Screenshots:** Take screenshots of your game at various stages (server setup, client connection, ship placement, gameplay, victory).
2.  **Graphics Software:** Use image editing software (like GIMP, Photoshop, or online tools like Canva) to create a game logo or other graphical elements.
3.  **Image Hosting:** Host your images on a platform like Imgur, GitHub Pages, or a personal website.
4.  **Replace Placeholders:** Update the `path/to/your_image.png` placeholders in the README with the actual URLs of your hosted images.

By adding images, you can make your README much more engaging and user-friendly.

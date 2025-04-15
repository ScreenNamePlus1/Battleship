 # Battleship Game (Local Two-Player)

This is a Python implementation of the classic Battleship game, where two players take turns on the same computer.

## How to Play

1.  **Run the Game:**
    * Open a terminal or command prompt.
    * Navigate to the directory containing the `battleship.py` file.
    * Run the script: `python battleship.py`

2.  **Player 1 Place Ships:**
    * Player 1 will be prompted to place their ships on the board.
    * Follow the on-screen instructions to enter coordinates and orientations for each ship.
    * Available ship sizes:
        * Carrier (5)
        * Battleship (4)
        * Cruiser (3)
        * Submarine (3)
        * Destroyer (2)
    * Valid orientations: H (horizontal) or V (vertical).
    * Valid coordinates: A1 - J10.

3.  **Player 2 Place Ships:**
    * Player 2 will then be prompted to place their ships on their board.

4.  **Take Turns:**
    * Players take turns guessing the coordinates of their opponent's ships.
    * Enter the coordinates of your shot (e.g., A5).
    * The game will indicate whether your shot was a hit or a miss.
    * If a ship is sunk, the game will announce which ship was sunk.

5.  **Win Condition:**
    * The first player to sink all of their opponent's ships wins the game.

6.  **Quitting**
    * Entering "Q" at the coordinates prompt will exit the game.

## Dependencies

* Python 3.x
* No external libraries are required (uses the standard `os` and `random` libraries).

## Notes

* This is a local two-player game, with players taking turns on the same computer.
* The game provides basic input validation.
* The game board is displayed in the terminal.

## Future Improvements

* Graphical user interface (GUI).
* Ability to save and load games.
* More robust error handling.
* Refined game logic and user interface.
* Network multiplayer.


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

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

import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    """Creates a 10x10 Battleship board."""
    return [['~' for _ in range(10)] for _ in range(10)]

def print_board(board):
    """Prints the Battleship board with coordinates."""
    print("  A B C D E F G H I J")
    for i, row in enumerate(board):
        print(f"{i+1:2} {' '.join(row)}")

def get_coordinates():
    """Gets valid coordinates from the player."""
    while True:
        try:
            coord = input("Enter coordinates (e.g., A5, or Q to quit): ").upper()
            if coord == 'Q':
                return 'Q', 'Q'  # Signal to quit
            if len(coord) < 2 or len(coord) > 3:
                print("Invalid Coordinates. Please enter coordinates like A5.")
                continue
            col = ord(coord[0]) - ord('A')
            row = int(coord[1:]) - 1
            if 0 <= col < 10 and 0 <= row < 10:
                return row, col
            else:
                print("Coordinates out of range. Please enter coordinates like A5.")
        except ValueError:
            print("Invalid input. Please enter coordinates like A5 or Q to quit.")

def display_available_placements(board, ship_size):
    """Displays available placement options for a ship."""
    available_placements = []
    for row in range(10):
        for col in range(10):
            if col + ship_size <= 10:  # Check horizontal
                valid_horizontal = True
                for i in range(ship_size):
                    if board[row][col + i] != '~':
                        valid_horizontal = False
                        break
                if valid_horizontal:
                    available_placements.append(f"{chr(col + ord('A'))}{row + 1} H")
            if row + ship_size <= 10:  # Check vertical
                valid_vertical = True
                for i in range(ship_size):
                    if board[row + i][col] != '~':
                        valid_vertical = False
                        break
                if valid_vertical:
                    available_placements.append(f"{chr(col + ord('A'))}{row + 1} V")
    if available_placements:
        print("Available placements:")
        for placement in available_placements:
            print(placement)
    else:
        print("No available placements for this ship.")

def place_ships(board, ships):
    """Places ships on the board."""
    for ship_name, ship_size in ships.items():
        print(f"Place your {ship_name} (size {ship_size}).")
        while True:
            display_available_placements(board, ship_size)
            row, col = get_coordinates()
            if row == 'Q':
                return False #quit signal.
            orientation = input("Enter orientation (H for horizontal, V for vertical): ").upper()
            valid_placement = True

            if orientation == 'H':
                if col + ship_size > 10:
                    valid_placement = False
                else:
                    for i in range(ship_size):
                        if board[row][col + i] != '~':
                            valid_placement = False
                            break
            elif orientation == 'V':
                if row + ship_size > 10:
                    valid_placement = False
                else:
                    for i in range(ship_size):
                        if board[row + i][col] != '~':
                            valid_placement = False
                            break
            else:
                valid_placement = False
                print("Invalid Orientation. Please enter H or V.")
                continue

            if valid_placement:
                if orientation == 'H':
                    for i in range(ship_size):
                        board[row][col + i] = 'S'  # 'S' represents a ship
                else:
                    for i in range(ship_size):
                        board[row + i][col] = 'S'
                break
            else:
                print("Invalid placement. Try again.")
        print_board(board)
    clear_screen()
    return True

def take_shot(board, opponent_board, ships):
    """Takes a shot at the opponent's board and checks for sunk ships."""
    row, col = get_coordinates()
    if row == 'Q':
        return 'Q' #quit signal.
    if opponent_board[row][col] == 'S':
        print("Hit!")
        board[row][col] = 'X'  # Mark hit
        opponent_board[row][col] = 'X'
        print_board(board)
        # Check if ship is sunk
        for ship_name, ship_size in ships.items():
            ship_coords = []
            for r in range(10):
                for c in range(10):
                    if opponent_board[r][c] == 'S':
                        ship_coords.append((r,c))
            sunk = True
            for r, c in ship_coords:
                if opponent_board[r][c] == 'S':
                    sunk = False
                    break
            if sunk and ship_size > 0 and len(ship_coords) == ship_size:
                print(f"You sunk the {ship_name}!")
                for r, c in ship_coords:
                    opponent_board[r][c] = 'x' #mark the ships positions as sunk.
                break
        return True
    else:
        print("Miss!")
        board[row][col] = 'O'  # Mark miss
        opponent_board[row][col] = 'O'
        print_board(board)
        return False

def check_win(board):
    """Checks if all ships are sunk."""
    for row in board:
        if 'S' in row:
            return False
    return True

# Game Setup
ships = {
    "Carrier": 5,
    "Battleship": 4,
    "Cruiser": 3,
    "Submarine": 3,
    "Destroyer": 2,
}

player1_board = create_board()
player2_board = create_board()
player1_shot_board = create_board()  # For player to track shots
player2_shot_board = create_board()

print("Player 1, place your ships:")
if not place_ships(player1_board, ships):
    print("Player 1 quit the game.")
    exit()

print("Player 2, place your ships:")
if not place_ships(player2_board, ships):
    print("Player 2 quit the game.")
    exit()

# Game Loop
current_player = 1
while True:
    print(f"\nPlayer {current_player}'s turn:")
    if current_player == 1:
        print("Player 1's shots:")
        print_board(player1_shot_board)
        shot_result = take_shot(player1_shot_board, player2_board, ships)
        if shot_result == 'Q':
            print("Player 1 quit the game.")
            break
        elif shot_result:
            if check_win(player2_board):
                print("Player 1 wins!")
                break
        else:
            current_player = 2
    else:
        print("Player 2's shots:")
        print_board(player2_shot_board)
        shot_result = take_shot(player2_shot_board, player1_board, ships)
        if shot_result == 'Q':
             print("Player 2 quit the game.")
             break
        elif shot_result:
            if check_win(player1_board):
                print("Player 2 wins!")
                break
        else:
            current_player = 1
    clear_screen()
                

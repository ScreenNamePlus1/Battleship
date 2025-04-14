import os

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
            coord = input("Enter coordinates (e.g., A5): ").upper()
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
            print("Invalid input. Please enter coordinates like A5.")

def place_ships(board, ships):
    """Places ships on the board."""
    for ship_name, ship_size in ships.items():
        print(f"Place your {ship_name} (size {ship_size}).")
        while True:
            row, col = get_coordinates()
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

def take_shot(board, opponent_board):
    """Takes a shot at the opponent's board."""
    row, col = get_coordinates()
    if opponent_board[row][col] == 'S':
        print("Hit!")
        board[row][col] = 'X'  # Mark hit
        opponent_board[row][col] = 'X'
        print_board(board) #display updated shot board.
        return True
    else:
        print("Miss!")
        board[row][col] = 'O'  # Mark miss
        opponent_board[row][col] = 'O'
        print_board(board) #display updated shot board.
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
place_ships(player1_board, ships)

print("Player 2, place your ships:")
place_ships(player2_board, ships)

# Game Loop
current_player = 1
while True:
    print(f"\nPlayer {current_player}'s turn:")
    if current_player == 1:
        print("Player 1's shots:")
        print_board(player1_shot_board)
        if take_shot(player1_shot_board, player2_board):
            if check_win(player2_board):
                print("Player 1 wins!")
                break
        else:
            current_player = 2
    else:
        print("Player 2's shots:")
        print_board(player2_shot_board)
        if take_shot(player2_shot_board, player1_board):
            if check_win(player1_board):
                print("Player 2 wins!")
                break
        else:
            current_player = 1
    clear_screen()

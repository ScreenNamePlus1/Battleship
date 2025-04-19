import socket
import json
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_board():
    return [['~' for _ in range(10)] for _ in range(10)]

def print_board(board):
    print("  A B C D E F G H I J")
    for i, row in enumerate(board):
        print(f"{i+1:2} {' '.join(row)}")

def get_coordinates(targeted_cells=None):
    if targeted_cells is None:
        targeted_cells = set()
    while True:
        try:
            coord = input("Enter coordinates (e.g., A5, or Q to quit): ").upper()
            if coord == 'Q':
                return 'Q', 'Q'
            if len(coord) < 2 or len(coord) > 3:
                print("Invalid Coordinates. Please enter coordinates like A5.")
                continue
            col_char = coord[0]
            row_num_str = coord[1:]
            if not col_char.isalpha() or not row_num_str.isdigit():
                print("Invalid input format. Please use letter-number format (e.g., A5).")
                continue
            col = ord(col_char) - ord('A')
            row = int(row_num_str) - 1
            if 0 <= col < 10 and 0 <= row < 10:
                if (row, col) in targeted_cells:
                    print("You have already targeted these coordinates. Choose again.")
                    continue
                return row, col
            else:
                print("Coordinates out of range. Please enter coordinates like A5.")
        except ValueError:
            print("Invalid input. Please enter coordinates like A5 or Q to quit.")

def display_available_placements(board, ship_size):
    available_placements = []
    for row in range(10):
        for col in range(10):
            if col + ship_size <= 10:
                valid_horizontal = True
                for i in range(ship_size):
                    if board[row][col + i] != '~':
                        valid_horizontal = False
                        break
                if valid_horizontal:
                    available_placements.append(f"{chr(col + ord('A'))}{row + 1} H")
            if row + ship_size <= 10:
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
    for ship_name, ship_size in ships.items():
        print(f"Place your {ship_name} (size {ship_size}).")
        while True:
            display_available_placements(board, ship_size)
            row, col = get_coordinates()
            if row == 'Q':
                return False
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
                        board[row][col + i] = 'S'
                else:
                    for i in range(ship_size):
                        board[row + i][col] = 'S'
                clear_screen()
                print("Your board:")
                print_board(board)
                break
            else:
                print("Invalid placement. Try again.")
    clear_screen()
    return True

def send_data(socket, data):
    try:
        serialized_data = json.dumps(data).encode()
        socket.sendall(serialized_data)
        return True
    except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
        print("Connection lost.")
        return False

def receive_data(socket):
    try:
        data = socket.recv(1024).decode()
        return json.loads(data)
    except (json.JSONDecodeError, ConnectionResetError, BrokenPipeError, ConnectionAbortedError):
        return None
    except socket.timeout:
        return None

def is_sunk(board, ship_parts):
    for r, c in ship_parts:
        if 0 <= r < 10 and 0 <= c < 10 and board[r][c] == 'S':
            return False
    return True

def update_sunk_ships(board, ships):
    sunk_ships = set()
    ship_locations = {}
    for r in range(10):
        for c in range(10):
            if board[r][c] == 'S':
                # Need a better way to identify individual ships
                pass # This requires more complex ship tracking

    # A more robust way would be to track ship placements explicitly
    # For simplicity, the current sinking logic in the main loop remains.
    return sunk_ships

def main():
    ships = {
        "Carrier": 5,
        "Battleship": 4,
        "Cruiser": 3,
        "Submarine": 3,
        "Destroyer": 2,
    }

    server_or_client = input("Do you want to be the server (S) or client (C)? ").upper()

    if server_or_client == 'S':
        host = socket.gethostbyname(socket.gethostname())
        port = 12345
        server_socket = socket.socket()
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")
        client_socket, address = server_socket.accept()
        print(f"Connection from: {address}")
        client_socket.settimeout(10) # Add timeout for receiving data

        player_board = create_board()
        if not place_ships(player_board, ships):
            print("Ship placement failed. Exiting.")
            return
        opponent_board = create_board()
        shot_board = create_board()
        targeted_cells = set()

        current_turn = 1
        while True:
            if current_turn == 1:
                print("\nYour shots:")
                print_board(shot_board)
                print("Your opponent's board:")
                print_board(opponent_board)
                row, col = get_coordinates(targeted_cells)
                if row == 'Q':
                    break
                targeted_cells.add((row, col))
                if not send_data(client_socket, {'row': row, 'col': col}):
                    break
                result = receive_data(client_socket)
                if result is None:
                    print("Opponent disconnected or timed out.")
                    break
                if result.get('hit'):
                    print("Hit!")
                    shot_board[row][col] = 'X'
                    opponent_board[row][col] = 'X'
                    if result.get('sunk'):
                        print(f"You sunk the {result['sunk']}!")
                else:
                    print("Miss!")
                    shot_board[row][col] = 'O'
                    opponent_board[row][col] = 'O'
                if all('S' not in row for row in opponent_board):
                    print("You won!")
                    break
                current_turn = 2
            else:
                print("\nWaiting for opponent's shot...")
                received_shot = receive_data(client_socket)
                if received_shot is None:
                    print("Opponent disconnected or timed out.")
                    break
                row, col = received_shot['row'], received_shot['col']
                print(f"Opponent shot at {chr(col + ord('A'))}{row + 1}.")
                hit = player_board[row][col] == 'S'
                sunk_ship = None
                if hit:
                    player_board[row][col] = 'X'
                    for ship_name, ship_size in ships.items():
                        ship_coords = []
                        for r in range(10):
                            for c in range(10):
                                if player_board[r][c] == 'S':
                                    ship_coords.append((r, c))
                        if ship_coords and is_sunk(player_board, ship_coords):
                            sunk_ship = ship_name
                            for r, c in ship_coords:
                                if 0 <= r < 10 and 0 <= c < 10:
                                    player_board[r][c] = 'x'
                            break

                send_data(client_socket, {'hit': hit, 'sunk': sunk_ship})
                print("Your board:")
                print_board(player_board)
                if all('S' not in row for row in player_board):
                    print("You lost!")
                    break
                current_turn = 1
        print("Game ended.")
        if client_socket:
            client_socket.close()
        if server_socket:
            server_socket.close()

    elif server_or_client == 'C':
        host = input("Enter server IP address: ")
        port = 12345
        client_socket = socket.socket()
        try:
            client_socket.connect((host, port))
            client_socket.settimeout(10) # Add timeout for receiving data
        except (socket.error, socket.timeout) as e:
            print(f"Could not connect to server: {e}")
            return

        player_board = create_board()
        if not place_ships(player_board, ships):
            print("Ship placement failed. Exiting.")
            return
        opponent_board = create_board()
        shot_board = create_board()
        targeted_cells = set()

        current_turn = 2
        while True:
            if current_turn == 2:
                print("\nYour shots:")
                print_board(shot_board)
                print("Your opponent's board:")
                print_board(opponent_board)
                row, col = get_coordinates(targeted_cells)
                if row == 'Q':
                    break
                targeted_cells.add((row, col))
                if not send_data(client_socket, {'row': row, 'col': col}):
                    break
                result = receive_data(client_socket)
                if result is None:
                    print("Server disconnected or timed out.")
                    break
                if result.get('hit'):
                    print("Hit!")
                    shot_board[row][col] = 'X'
                    opponent_board[row][col] = 'X'
                    if result.get('sunk'):
                        print(f"You sunk the {result['sunk']}!")
                else:
                    print("Miss!")
                    shot_board[row][col] = 'O'
                    opponent_board[row][col] = 'O'
                if all('S' not in row for row in opponent_board):
                    print("You won!")
                    break
                current_turn = 1
            else:
                print("\nWaiting for opponent's shot...")
                received_shot = receive_data(client_socket)
                if received_shot is None:
                    print("Server disconnected or timed out.")
                    break
                row, col = received_shot['row'], received_shot['col']
                print(f"Opponent shot at {chr(col + ord('A'))}{row + 1}.")
                hit = player_board[row][col] == 'S'
                sunk_ship = None
                if hit:
                    player_board[row][col] = 'X'
                    for ship_name, ship_size in ships.items():
                        ship_coords = []
                        for r in range(10):
                            for c in range(10):
                                if player_board[r][c] == 'S':
                                    ship_coords.append((r, c))
                        if ship_coords and is_sunk(player_board, ship_coords):
                            sunk_ship = ship_name
                            for r, c in ship_coords:
                                if 0 <= r < 10 and 0 <= c < 10:
                                    player_board[r][c] = 'x'
                            break
                send_data(client_socket, {'hit': hit, 'sunk': sunk_ship})
                print("Your board:")
                print_board(player_board)
                if all('S' not in row for row in player_board):
                    print("You lost!")
                    break
                current_turn = 2
        print("Game ended.")
        client_socket.close()

    else:
        print("Invalid input. Please enter S or C.")

if __name__ == "__main__":
    main()

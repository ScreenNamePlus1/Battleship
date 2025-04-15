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

def get_coordinates():
    while True:
        try:
            coord = input("Enter coordinates (e.g., A5, or Q to quit): ").upper()
            if coord == 'Q':
                return 'Q', 'Q'
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
                break
            else:
                print("Invalid placement. Try again.")
        print_board(board)
    clear_screen()
    return True

def send_data(socket, data):
    try:
        serialized_data = json.dumps(data).encode()
        socket.send(serialized_data)
        return True
    except (BrokenPipeError, ConnectionResetError):
        print("Connection lost.")
        return False

def receive_data(socket):
    try:
        data = socket.recv(1024).decode()
        return json.loads(data)
    except (json.JSONDecodeError, ConnectionResetError, BrokenPipeError):
        return None

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
        player_board = create_board()
        place_ships(player_board, ships)
        opponent_board = create_board()
        shot_board = create_board()

        current_turn = 1
        while True:
            if current_turn == 1:
                print("Your shots:")
                print_board(shot_board)
                row, col = get_coordinates()
                if row == 'Q':
                    break
                if not send_data(client_socket, {'row': row, 'col': col}):
                    break
                result = receive_data(client_socket)
                if result is None:
                    break
                if result['hit']:
                    print("Hit!")
                    shot_board[row][col] = 'X'
                    opponent_board[row][col] = 'X'
                    if result.get('sunk'):
                        print(f"You sunk the {result['sunk']}!")
                else:
                    print("Miss!")
                    shot_board[row][col] = 'O'
                    opponent_board[row][col] = 'O'
                current_turn = 2
            else:
                received_shot = receive_data(client_socket)
                if received_shot is None:
                    break
                row, col = received_shot['row'], received_shot['col']
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
                        sunk = True
                        for r, c in ship_coords:
                            if player_board[r][c] == 'S':
                                sunk = False
                                break
                        if sunk and ship_size > 0 and len(ship_coords) == ship_size:
                            sunk_ship = ship_name
                            for r, c in ship_coords:
                                player_board[r][c] = 'x'
                            break

                send_data(client_socket, {'hit': hit, 'sunk': sunk_ship})
                if all('S' not in row for row in player_board):
                    print("You lost!")
                    break
                current_turn = 1
        client_socket.close()
        server_socket.close()

    elif server_or_client == 'C':
        host = input("Enter server IP address: ")
        port = 12345
        client_socket = socket.socket()
        client_socket.connect((host, port))
        player_board = create_board()
        place_ships(player_board, ships)
        opponent_board = create_board()
        shot_board = create_board()

        current_turn = 2
        while True:
            if current_turn == 2:
                print("Your shots:")
                print_board(shot_board)
                row, col = get_coordinates()
                if row == 'Q':
                    break
                if not send_data(client_socket, {'row': row, 'col': col}):
                    break
                result = receive_data(client_socket)
                if result is None:
                    break
                if result['hit']:
                    print("Hit!")
                    shot_board[row][col] = 'X'
                    opponent_board[row][col] = 'X'
                    if result.get('sunk'):
                        print(f"You sunk the {result['sunk']}!")
                else:
                    print("Miss!")
                    shot_board[row][col] = 'O'
                    opponent_board[row][col] = 'O'
                current_turn = 1
            else:
                received_shot = receive_data(client_socket)
                if received_shot is None:
                    break
                row, col = received_shot['row'], received_shot['col']
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
                        sunk = True
                        for r, c in ship_coords:
                            if player_board[r][c] == 'S':
                                sunk = False
                                break
                        if sunk and ship_size > 0 and len(ship_coords) == ship_size:
                            sunk_ship = ship_name
                            for r, c in ship_coords:
                                player_board[r][c] = 'x'
                            break
                send_data(client_socket, {'hit': hit, 'sunk': sunk_ship})
                if all('S' not in row for row in player_board):
                    print("You lost!")
                    break
                current_turn = 2
        client_socket.close()
    else:
        print("Invalid input. Please enter S or C.")

if __name__ == "__main__":
    main()

import os

def print_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    win_positions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for pos in win_positions:
        if all(board[i] == player for i in pos):
            return True
    return False

def save_game(board, current_player):
    with open("game_state.txt", "w") as file:
        file.write(",".join(board) + "\n")
        file.write(current_player + "\n")

def load_game():
    try:
        with open("game_state.txt", "r") as file:
            lines = file.readlines()
            board = lines[0].strip().split(",")
            current_player = lines[1].strip()
            return board, current_player
    except FileNotFoundError:
        return None, None

def is_draw(board):
    return all(cell != " " for cell in board)

def main():
    board, current_player = load_game()
    if not board:
        board = [" " for _ in range(9)]
        current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        try:
            move = int(input("Enter your move (1-9) or 0 to save and exit: "))
            if move == 0:
                save_game(board, current_player)
                print("Game saved! Exiting...")
                break
            if move < 1 or move > 9 or board[move - 1] != " ":
                print("Invalid move. Try again.")
                continue
            board[move - 1] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

if __name__ == "__main__":
    main()

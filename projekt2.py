"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Matěj Adámek
email: matej.311@seznam.cz
discord: Addy#8986
"""
def print_board(gameBoard):
    """Prints the Tic Tac Toe board."""
    rows, cols = len(gameBoard), len(gameBoard[0])
    for x in range(rows):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(cols):
            print("", gameBoard[x][y], end=" |")
    print("\n+---+---+---+")


def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)


def tic_tac_toe():
    print("Welcome to Tic Tac Toe")
    print("="*44)
    print("GAME RULES:")
    print("Each player can place one mark (or stone)")
    print("per turn on the 3x3 grid. The WINNER is")
    print("who succeeds in placing three of their")
    print("marks in a:")
    print("* horizontal,")
    print("* vertical or")
    print("* diagonal row")
    print("=" * 44)
    print("Let's start the game")

    # Initialize the board
    gameBoard = [[" " for _ in range(3)] for _ in range(3)]

    # Player symbols
    players = ['X', 'O']
    current_player = 0

    # Main game loop
    while True:
        print("="*44)
        print_board(gameBoard)
        print(f"Player {players[current_player]} | Please enter your move number:")

        try:
            move = int(input())
            row = (move - 1) // 3
            col = (move - 1) % 3

            if gameBoard[row][col] != ' ':
                print("Invalid move. Cell already taken.")
                continue

            gameBoard[row][col] = players[current_player]

            if check_win(gameBoard, players[current_player]):
                print("="*44)
                print_board(gameBoard)
                print(f"Congratulations, the player {players[current_player]} WON!")
                break

            if is_board_full(gameBoard):
                print("="*44)
                print_board(gameBoard)
                print("It's a draw!")
                break

            current_player = 1 - current_player  # Switch player
        except ValueError:
            print("Invalid input. Please enter a valid number (1-9).")
        except IndexError:
            print("Invalid input. Please enter a number between 1 and 9.")


if __name__ == "__main__":
    tic_tac_toe()

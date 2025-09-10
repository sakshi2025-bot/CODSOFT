import math

# A function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("---------")
    print("\n")

# A function to check for a win
def check_win(board, player):
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# A function to check for a draw
def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

# The Minimax algorithm
def minimax(board, is_maximizing):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "X"  # X is the AI player
                    score = minimax(board, False)
                    board[r][c] = " "  # Undo the move
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for r in range(3):
            for c in range(3):
                if board[r][c] == " ":
                    board[r][c] = "O"  # O is the human player
                    score = minimax(board, True)
                    board[r][c] = " "  # Undo the move
                    best_score = min(score, best_score)
        return best_score

# A function to find the best move for the AI using Minimax
def find_best_move(board):
    best_score = -math.inf
    best_move = (-1, -1)
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                board[r][c] = "X"
                score = minimax(board, False)
                board[r][c] = " "
                if score > best_score:
                    best_score = score
                    best_move = (r, c)
    return best_move

# The main game function
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "O"  # Human player starts

    print("Welcome to Tic-Tac-Toe! You are 'O', and the AI is 'X'.")
    print("Enter your moves as row and column (e.g., 1 2 for top-right).")

    while True:
        print_board(board)
        
        if current_player == "O":
            while True:
                try:
                    move = input("Your move (row col): ").split()
                    row, col = int(move[0]) - 1, int(move[1]) - 1
                    if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                        board[row][col] = current_player
                        break
                    else:
                        print("Invalid move. Please try again.")
                except (ValueError, IndexError):
                    print("Invalid input. Please enter two numbers separated by a space.")
            
            if check_win(board, "O"):
                print_board(board)
                print("Congratulations! You won! 🎉")
                break
            
            current_player = "X"
        
        else:  # AI's turn
            print("AI's turn...")
            row, col = find_best_move(board)
            board[row][col] = "X"
            print(f"AI plays at ({row + 1}, {col + 1})")
            
            if check_win(board, "X"):
                print_board(board)
                print("The AI won! You can't beat me! 🤖")
                break
            
            current_player = "O"

        if check_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

if __name__ == "__main__":
    main()
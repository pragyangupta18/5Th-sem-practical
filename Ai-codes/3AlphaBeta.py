# Tic-Tac-Toe board is represented as a 2D list
# 'X' represents the player, 'O' represents the opponent, and ' ' represents an empty cell

def evaluate(board):
    # Evaluate the board and return the game's outcome:
    # 1 if the player wins, -1 if the opponent wins, 0 for a tie, and None for an ongoing game.
    
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return 1 if board[i][0] == 'X' else -1
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return 1 if board[0][i] == 'X' else -1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 1 if board[0][0] == 'X' else -1
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 1 if board[0][2] == 'X' else -1

    # Check for a tie
    if ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
        return 0

    return None  # Game is still ongoing

def minimax(board, depth, is_max, alpha, beta):
    # Base case: terminal node or maximum depth reached
    result = evaluate(board)
    if result is not None:
        return result

    if is_max:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def find_best_move(board):
    best_move = (-1, -1)
    best_score = -float("inf")

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -float("inf"), float("inf"))
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    
    return best_move

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    while evaluate(board) is None:
        print_board(board)
        player_row, player_col = map(int, input("Enter your move (row and column, space-separated): ").split())
        if board[player_row][player_col] == ' ':
            board[player_row][player_col] = 'O'
        else:
            print("Invalid move. Try again.")
            continue
        
        if evaluate(board) is not None:
            break

        print_board(board)
        print("AI's move:")
        ai_row, ai_col = find_best_move(board)
        board[ai_row][ai_col] = 'X'
    
    result = evaluate(board)
    print_board(board)
    if result == 1:
        print("You lose! AI wins.")
    elif result == -1:
        print("Congratulations! You win.")
    else:
        print("It's a tie!")

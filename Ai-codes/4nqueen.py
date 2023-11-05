# Function to check if a queen can be placed on the board at a given position
def is_safe(board, row, col, n):
    # Check the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Function to solve the N-Queens problem using Backtracking and Branch and Bound
def solve_n_queens(n):
    def solve_util(board, col):
        if col >= n:
            return True
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                if solve_util(board, col + 1):
                    return True
                board[i][col] = 0
        return False

    board = [[0 for _ in range(n)] for _ in range(n)]

    if not solve_util(board, 0):
        print("No solution exists.")
        return

    # Print the solution
    for row in board:
        print(' '.join(['Q' if cell == 1 else '.' for cell in row]))

# Get user input for the board size (N)
n = int(input("Enter the No.of Queen (N): "))
solve_n_queens(n)

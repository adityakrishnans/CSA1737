# 8-Queen Problem using Backtracking

N = 8

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_queens(board, row):
    if row == N:
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve_queens(board, row + 1):
                return True
    return False

# ---- DRIVER CODE ----
board = [-1] * N

if solve_queens(board, 0):
    print("Solution for 8-Queen Problem:")
    for r in range(N):
        row = ""
        for c in range(N):
            row += " Q " if board[r] == c else " . "
        print(row)
else:
    print("No solution exists.")

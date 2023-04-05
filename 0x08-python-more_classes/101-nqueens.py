#!/usr/bin/python3
import sys

def is_valid(board, row, col, n):
    # Check if there is any queen in the same row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is any queen in the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is any queen in the lower diagonal on the left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve(board, col, n):
    # Base case: all queens are placed
    if col == n:
        for row in board:
            print(' '.join(str(x) for x in row))
        print()
        return True

    # Recursive case: try to place a queen in each row of the current column
    for i in range(n):
        if is_valid(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n)
            board[i][col] = 0

    return False

if __name__ == '__main__':
    # Parse command line arguments
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Initialize board
    board = [[0 for j in range(n)] for i in range(n)]

    # Solve the problem
    solve(board, 0, n)

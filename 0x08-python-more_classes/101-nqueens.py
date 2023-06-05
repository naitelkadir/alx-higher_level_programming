#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i][col] == 'Q':
            return (False)
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return (False)
        i -= 1
        j -= 1
    i, j = row, col
    while i >= 0 and j < N:
       if board[i][j] == 'Q':
           return (False)
       i -= 1
       j += 1
    return True
def solve_nqueens(board, row, N, solutions):
    if row == N:
        solution = []
        for i in range(N):
            queen_pos = [i, board[i].index('Q')]
            solution.append(queen_pos)
        solutions.append(solution)
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 'Q'
            solve_nqueens(board, row + 1, N, solutions)
            board[row][col] = '.'
def nqueens(N):
    if not  N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [['.' for _ in range(N)] for _ in range (N)]
    solutions = []
    solve_nqueens(board, 0, N, solutions)
    for solution in solutions:
        print(solution)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])

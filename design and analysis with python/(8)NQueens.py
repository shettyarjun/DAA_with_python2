def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1 or \
           (col - (row - i) >= 0 and board[i][col - (row - i)] == 1) or \
           (col + (row - i) < n and board[i][col + (row - i)] == 1):
            return False
    return True


def solve_n_queens(n):
    solutions = []

    def backtrack(row, board):
        if row == n:
            solutions.append([row[:] for row in board])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(row + 1, board)
                board[row][col] = 0

    board = [[0] * n for _ in range(n)]
    backtrack(0, board)
    return solutions

def print_solutions(solutions):
    if solutions:
        for sol in solutions:
            for row in sol:
                print(' '.join(map(str, row)))
            print()
    else:
        print("No solutions found.")

N = int(input("Enter the value of N: "))
print_solutions(solve_n_queens(N))

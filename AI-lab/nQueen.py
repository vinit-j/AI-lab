import random

def initialize_board(n):
    board = [-1] * n
    for i in range(n):
        while True:
            col = random.randint(0, n - 1)
            if col not in board:
                board[i] = col
                break
    return board

def print_board(board):
    for row in range(len(board)):
        line = ""
        for col in range(len(board)):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def count_conflicts(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

def heuristic(board):
    return count_conflicts(board)

def solve_queen_problem(n):
    current_board = initialize_board(n)
    current_heuristic = heuristic(current_board)

    while current_heuristic > 0:
        next_board = list(current_board)
        for row in range(n):
            for col in range(n):
                if current_board[row] != col:
                    next_board[row] = col
                    next_heuristic = heuristic(next_board)
                    if next_heuristic < current_heuristic:
                        current_board = list(next_board)
                        current_heuristic = next_heuristic

        if current_heuristic == 0:
            return current_board

if __name__ == "__main__":
    n = 8  # Number of queens
    solution = solve_queen_problem(n)
    
    if solution:
        print("Solution found:")
        print_board(solution)
    else:
        print("No solution found.")

import random

class Puzzle8:
    def __init__(self, initial_state):
        self.goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
        self.state = initial_state

    def print_state(self):
        for i in range(0, 9, 3):
            print(self.state[i:i+3])

    def find_blank(self):
        return self.state.index(0)

    def generate_neighbors(self):
        blank_index = self.find_blank()
        neighbors = []

        # Possible moves: up, down, left, right
        moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move in moves:
            x, y = move
            new_index = blank_index + (3 * x) + y

            if 0 <= new_index < 9:
                new_state = list(self.state)
                new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
                neighbors.append(new_state)

        return neighbors

    def heuristic(self):
        # Misplaced tiles heuristic
        return sum([1 if self.state[i] != self.goal_state[i] else 0 for i in range(9)])

    def solve(self):
        while True:
            current_heuristic = self.heuristic()
            if current_heuristic == 0:
                print("Goal state reached:")
                self.print_state()
                break

            neighbors = self.generate_neighbors()
            best_neighbor = None
            best_heuristic = float('inf')

            for neighbor in neighbors:
                neighbor_heuristic = Puzzle8(neighbor).heuristic()
                if neighbor_heuristic < best_heuristic:
                    best_neighbor = neighbor
                    best_heuristic = neighbor_heuristic

            if best_heuristic >= current_heuristic:
                print("Stuck in local minimum:")
                self.print_state()
                break

            self.state = best_neighbor

if __name__ == "__main__":
    # Initialize the puzzle with a random initial state
    initial_state = random.sample(range(9), 9)
    puzzle = Puzzle8(initial_state)

    print("Initial state:")
    puzzle.print_state()

    print("\nSolving...")
    puzzle.solve()

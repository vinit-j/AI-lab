import heapq

class WaterJugProblem:
    def __init__(self, capacity_x, capacity_y, target):
        self.capacity_x = capacity_x
        self.capacity_y = capacity_y
        self.target = target
        self.visited = set()
        self.actions = [(0, 'Fill X'), (1, 'Fill Y'), (2, 'Empty X'), (3, 'Empty Y'), (4, 'Pour X to Y'), (5, 'Pour Y to X')]

    def is_valid_state(self, state):
        x, y = state
        return 0 <= x <= self.capacity_x and 0 <= y <= self.capacity_y

    def get_neighbors(self, state):
        x, y = state
        neighbors = []

        # Fill X
        neighbors.append((self.capacity_x, y))

        # Fill Y
        neighbors.append((x, self.capacity_y))

        # Empty X
        neighbors.append((0, y))

        # Empty Y
        neighbors.append((x, 0))

        # Pour X to Y
        pour_x_to_y = min(x, self.capacity_y - y)
        neighbors.append((x - pour_x_to_y, y + pour_x_to_y))

        # Pour Y to X
        pour_y_to_x = min(y, self.capacity_x - x)
        neighbors.append((x + pour_y_to_x, y - pour_y_to_x))

        return [neighbor for neighbor in neighbors if self.is_valid_state(neighbor)]

    def heuristic(self, state):
        # Use a heuristic function to estimate the cost to reach the target state.
        x, y = state
        return abs(x - self.target) + abs(y - self.target)

    def best_first_search(self):
        start_state = (0, 0)
        priority_queue = [(self.heuristic(start_state), start_state, [])]

        while priority_queue:
            _, current_state, path = heapq.heappop(priority_queue)

            if current_state == (self.target, self.target):
                return path

            if current_state in self.visited:
                continue

            self.visited.add(current_state)

            for action_index, action_name in self.actions:
                next_state = self.get_neighbors(current_state)[action_index]
                if next_state not in self.visited:
                    next_path = path + [action_name]
                    cost = len(next_path) + self.heuristic(next_state)
                    heapq.heappush(priority_queue, (cost, next_state, next_path))

        return None

    def solve(self):
        result = self.best_first_search()
        if result:
            print("Solution found:")
            for step, action in enumerate(result):
                print(f"Step {step + 1}: {action}")
        else:
            print("No solution found.")

# Example usage:
if __name__ == "__main__":
    capacity_x = 4  # Capacity of jug X
    capacity_y = 3  # Capacity of jug Y
    target = 2      # Target amount of water to measure

    water_jug_problem = WaterJugProblem(capacity_x, capacity_y, target)
    water_jug_problem.solve()

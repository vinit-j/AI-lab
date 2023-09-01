import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        # Compare nodes based on their total estimated cost.
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def ao_star(initial_state, goal_state, actions, successor, heuristic):
    open_set = []
    closed_set = set()

    initial_node = Node(initial_state, None, 0, heuristic(initial_state, goal_state))
    heapq.heappush(open_set, initial_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal_state:
            return reconstruct_path(current_node)

        closed_set.add(current_node.state)

        for action in actions(current_node.state):
            next_state = successor(current_node.state, action)
            if next_state not  in closed_set:
                g_cost = current_node.cost + 1  # Assuming a uniform cost of 1 for all actions
                h_cost = heuristic(next_state, goal_state)
                child_node = Node(next_state, current_node, g_cost, h_cost)

                if not any(node for node in open_set if node.state == next_state and node.cost <= g_cost):
                    heapq.heappush(open_set, child_node)

    return None

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

#Driver Code
if __name__ == "__main__":
    initial_state = "S"
    goal_state = "G"
    actions = lambda state: ["A", "B"] if state == "S" else []
    successor = lambda state, action: "G" if action == "A" else "S"
    heuristic = lambda state, goal: 1 if state != goal else 0

    result = ao_star(initial_state, goal_state, actions, successor, heuristic)

    if result:
        print("Path found:", result)
    else:
        print("No solution found.")

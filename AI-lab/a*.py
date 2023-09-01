import itertools
import heapq

class TSP:
    def __init__(self, cities):
        self.cities = cities
        self.num_cities = len(cities)
        self.distances = self.calculate_distances()
        self.initial_state = (0, tuple(range(1, self.num_cities)))

    def calculate_distances(self):
        distances = {}
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    distances[(i, j)] = self.calculate_distance(self.cities[i], self.cities[j])
        return distances

    def calculate_distance(self, city1, city2):
        return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5

    def heuristic(self, state):
        # Minimum spanning tree heuristic.
        total_distance = 0
        remaining_cities = list(state[1])
        current_city = 0  # Starting from city 0

        while remaining_cities:
            min_distance = float('inf')
            nearest_city = None

            for city in remaining_cities:
                distance = self.distances[(current_city, city)]
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city

            total_distance += min_distance
            remaining_cities.remove(nearest_city)
            current_city = nearest_city

        # Add the distance from the last city back to the starting city.
        total_distance += self.distances[(current_city, 0)]

        return total_distance

    def a_star_search(self):
        priority_queue = [(self.heuristic(self.initial_state), 0, self.initial_state)]
        visited = set()

        while priority_queue:
            _, cost, current_state = heapq.heappop(priority_queue)

            if len(current_state[1]) == 0:
                return cost + self.distances[(current_state[0], 0)]

            if current_state in visited:
                continue

            visited.add(current_state)

            for next_city in current_state[1]:
                new_state = (next_city, tuple(filter(lambda x: x != next_city, current_state[1])))
                new_cost = cost + self.distances[(current_state[0], next_city)]
                priority = new_cost + self.heuristic(new_state)
                heapq.heappush(priority_queue, (priority, new_cost, new_state))

        return None

if __name__ == "__main__":
    cities = [(0, 0), (2, 4), (3, 1), (1, 3)]
    tsp = TSP(cities)
    shortest_distance = tsp.a_star_search()
    
    if shortest_distance:
        print("Shortest distance:", shortest_distance)
    else:
        print("No solution found.")

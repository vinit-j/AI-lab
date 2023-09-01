from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)

                if node in self.graph:
                    neighbors = self.graph[node]
                    for neighbor in neighbors:
                        if neighbor not in visited:
                            queue.append(neighbor)

        return result

#DriverCode
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('F', 'G')

    start_node = 'A'
    bfs_result = g.bfs(start_node)

    print("Breadth-First Search starting from node", start_node)
    print("Result:", bfs_result)

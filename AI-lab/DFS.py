class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)

        print(start, end=' ')

        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs(neighbor, visited)

#Driver Code:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    g.add_edge('F', 'G')

    start_node = 'A'
    print("Depth-First Search starting from node", start_node)
    g.dfs(start_node)

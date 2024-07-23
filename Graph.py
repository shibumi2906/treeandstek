class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = [start]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                print(vertex, end=' ')
                visited.add(vertex)
                queue.extend(set(self.graph[vertex]) - visited)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                self._dfs_recursive(neighbor, visited)

# Пример использования графа
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS начиная с вершины 2:")
g.bfs(2)  # Вывод: 2 0 3 1

print("\nDFS начиная с вершины 2:")
g.dfs(2)  # Вывод: 2 0 1 3

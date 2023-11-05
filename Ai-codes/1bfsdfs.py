# Implement depth-first search algorithm and Breadth First Search algorithm.
# Use an undirected graph and develop a recursive algorithm for searching all the vertices of a graph or tree data structure.

graph = {}

num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter a vertex: ")
    adjacents = input("Enter adjacent vertices (comma-separated): ").split(',')
    graph[vertex] = [v.strip() for v in adjacents]

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph.get(node, []):
            dfs(visited, graph, neighbor)

from collections import deque


def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            queue.extend(neighbor for neighbor in graph.get(node, []) if neighbor not in visited)

start_node = input("Enter the starting node: ")

print("Depth-First Search:")
dfs(visited, graph, start_node)

visited = set()

print("Breadth-First Search:")
bfs(graph, start_node)

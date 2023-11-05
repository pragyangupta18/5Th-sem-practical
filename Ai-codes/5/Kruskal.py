
import heapq
from collections import defaultdict

def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            mst[frm].add(to)
            for to_next, cost2 in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost2, to, to_next))

    return mst

# Define your graph as an adjacency list
graph = {
    'A': {'B': 4, 'C': 8},
    'B': {'A': 4, 'C': 2, 'D': 5},
    'C': {'A': 8, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Specify the starting vertex for the MST
starting_vertex = 'A'

# Call the function to create the minimum spanning tree
minimum_spanning_tree = create_spanning_tree(graph, starting_vertex)

# Print the minimum spanning tree
for vertex, adjacent_vertices in minimum_spanning_tree.items():
    for adj_vertex in adjacent_vertices:
        print(f'Edge: {vertex} - {adj_vertex}, Cost: {graph[vertex][adj_vertex]}')

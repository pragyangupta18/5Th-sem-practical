"""8. Implement Greedy search algorithm for any of the following application:
 • Dijkstra’s Minimum Spanning Tree Algorithm
"""
import heapq

def dijkstra(graph, source):
    distance = {node: float('infinity') for node in graph}
    distance[source] = 0
    queue = [(0, source)]
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance_through_current_node = current_distance + weight

            if distance_through_current_node < distance[neighbor]:
                distance[neighbor] = distance_through_current_node
                heapq.heappush(queue, (distance[neighbor], neighbor))

    return distance

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_node = 'A'
distances = dijkstra(graph, source_node)

for node, distance in distances.items():
    path = []
    current_node = node
    while current_node != source_node:
        path.append(current_node)
        current_node = min(graph[current_node], key=lambda x: distances[x] + graph[current_node][x])
    path.append(source_node)
    path.reverse()
    path_str = ' -> '.join(path)
    print(f"Shortest path from {source_node} to {node}: {path_str} (Distance: {distance})")

    """
Output
Shortest path from A to A: A (Distance: 0)
Shortest path from A to B: A -> B (Distance: 1)
Shortest path from A to C: A -> B -> C (Distance: 3)
Shortest path from A to D: A -> B -> C -> D (Distance: 4)
"""

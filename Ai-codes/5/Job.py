"""Implement Greedy search algorithm for any of the following application:
 • Single-Source Shortest Path Problem 
• Job Scheduling Problem
"""
#Single-Source Shortest Path Problem Dijkstra's algorithm and Bellman-Ford algorithm are common approaches for solving the SSSP problem.
#dijkstra 
import heapq
def dijkstra(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph represented as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}
source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)

# Display the shortest distances from the source vertex
for vertex, distance in shortest_distances.items():
    print(f'Shortest distance from {source_vertex} to {vertex}: {distance}')


#Job Scheduling Problem
def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[1])
    
    n = len(jobs)
    dp = [0] * n
    
    for i in range(1, n):
        dp[i] = max(jobs[i][2], dp[i - 1])
        for j in range(i - 1, -1, -1):
            if jobs[i][1] <= jobs[j][0]:
                dp[i] = max(dp[i], jobs[i][2] + dp[j])
                break
    
    max_profit = max(dp)
    return max_profit

# Example jobs: (start_time, finish_time, profit)
#jobs = [(1, 3, 5), (2, 5, 6), (6, 8, 7), (4, 7, 8), (5, 9, 9)]
# Accept user input for job scheduling
jobs = []
num_jobs = int(input("Enter the number of jobs: "))

for i in range(num_jobs):
    start_time = int(input(f"Enter the start time for job {i + 1}: "))
    finish_time = int(input(f"Enter the finish time for job {i + 1}: "))
    profit = int(input(f"Enter the profit for job {i + 1}: "))
    jobs.append((start_time, finish_time, profit))

max_profit = job_scheduling(jobs)
print(f"Maximum profit: {max_profit}")

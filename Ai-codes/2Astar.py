import heapq

# Define directions for 4 neighbors: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def heuristic(node, goal):
    # Calculate the Manhattan distance as the heuristic
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def find_path(grid, start, goal):
    # Initialize the open list with the start node and cost
    open_list = [(0, start)]
    # Initialize the closed list
    closed_list = set()
    # Create a dictionary to keep track of parent nodes
    parent = {}

    # Create a dictionary to store the cost to reach each node from the start
    g_score = {}
    g_score[start] = 0

    # Main loop
    while open_list:
        # Pop the node with the lowest f-score
        current_f, current_node = heapq.heappop(open_list)
        
        # If the current node is the goal, reconstruct the path and return it
        if current_node == goal:
            path = []
            while current_node in parent:
                path.insert(0, current_node)
                current_node = parent[current_node]
            return path
        
        # Add the current node to the closed list
        closed_list.add(current_node)

        # Explore neighbors
        for direction in directions:
            dx, dy = direction
            neighbor = (current_node[0] + dx, current_node[1] + dy)

            # Check if the neighbor is within bounds and not blocked
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] != 1:
                # Calculate the tentative g-score
                tentative_g = g_score[current_node] + 1
                
                # Check if the neighbor is already in the closed list and the new path is not better
                if neighbor in closed_list and tentative_g >= g_score.get(neighbor, float('inf')):
                    continue
                
                if tentative_g < g_score.get(neighbor, float('inf')):
                    parent[neighbor] = current_node
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score, neighbor))

    # If no path is found, return None
    return None

# Input from the user
print("Enter the grid (0 for empty, 1 for obstacle):")
grid = []
for i in range(5):
    row = list(map(int, input().split()))
    grid.append(row)

start = tuple(map(int, input("Enter the start position (row column): ").split()))
goal = tuple(map(int, input("Enter the goal position (row column): ").split()))

path = find_path(grid, start, goal)
if path:
    print("Path found:", path)
else:
    print("No path found")

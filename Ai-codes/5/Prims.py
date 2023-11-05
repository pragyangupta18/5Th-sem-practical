"""
6 Implement Greedy search algorithm for any of the following application:
 • Prim's Minimal Spanning Tree Algorithm
"""
V = int(input("Enter the number of vertices: "))
G = [[0] * V for _ in range(V)]

print("Enter the weight for each edge (0 for no connection):")
for i in range(V):
    for j in range(i + 1, V):
        weight = int(input(f"Enter the weight for edge {i}-{j}: "))
        G[i][j] = G[j][i] = weight

selected, cost = [0], 0

print("Edge : Weight\n")
while len(selected) < V:
    minimum = float("inf")
    a, b = 0, 0
    for i in selected:
        for j in range(V):
            if j not in selected and G[i][j] > 0 and G[i][j] < minimum:
                minimum = G[i][j]
                a, b = i, j
    selected.append(b)
    cost += minimum
    print(f"{a}-{b}: {minimum}")

print(f"Minimum Cost: {cost}")


"""
Enter the number of vertices: 5

Enter the weight for edge 0-1: 9
Enter the weight for edge 0-2: 75
Enter the weight for edge 0-3: 0
Enter the weight for edge 0-4: 0
Enter the weight for edge 1-2: 95
Enter the weight for edge 1-3: 19
Enter the weight for edge 1-4: 42
Enter the weight for edge 2-3: 51
Enter the weight for edge 2-4: 66
Enter the weight for edge 3-4: 31
The output will be:

Edge : Weight

0-1: 9
1-3: 19
3-4: 31
0-2: 75
Minimum Cost: 134


"""
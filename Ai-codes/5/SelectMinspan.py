"""Implement Greedy search algorithm for any of the following application: 
 Selection Sort 
 Minimum Spanning Tree 
"""
#Selection SOrt
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in the unsorted portion of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [89,56,90,1,4,6]
selection_sort(arr)
print("Sorted array is:", arr)

# Minimum Spanning Tree 
# Prim's Algorithm in Python
INF = 9999999
# number of vertices in graph
V = 5

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]
# set number of edge to 0
no_edge = 0

selected[0] = True
# print for edge and weight
print("Edge : Weight\n")
while (no_edge < V - 1):
 
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + "-" + str(y) + ":" + str(G[x][y]))
    selected[y] = True
    no_edge += 1
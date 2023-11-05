class GraphColoring:
    def __init__(self, graph, colors, color_names):
        self.graph = graph
        self.colors = colors
        self.color_names = color_names  # Added color names
        self.num_vertices = len(graph)
        self.solution = [0] * self.num_vertices  # Initialize with no colors assigned
        self.best_solution = [0] * self.num_vertices  # Best solution found so far
        self.min_conflicts = float('inf')  # Minimum number of conflicts

    def is_safe(self, vertex, color, c):
        for neighbor in range(self.num_vertices):
            if self.graph[vertex][neighbor] == 1 and self.solution[neighbor] == color:
                return False
        return True

    def backtrack(self, vertex):
        if vertex == self.num_vertices:
            # All vertices have been colored without conflicts
            conflicts = self.count_conflicts()
            if conflicts < self.min_conflicts:
                self.min_conflicts = conflicts
                self.best_solution = self.solution.copy() 
            return

        for color in range(self.colors):
            if self.is_safe(vertex, color, vertex):
                self.solution[vertex] = color
                self.backtrack(vertex + 1)
                self.solution[vertex] = 0  # Backtrack

    def count_conflicts(self):
        conflicts = 0
        for vertex in range(self.num_vertices):
            for neighbor in range(self.num_vertices):
                if self.graph[vertex][neighbor] == 1 and self.solution[vertex] == self.solution[neighbor]:
                    conflicts += 1
        return conflicts

    def branch_and_bound(self):
        self.backtrack(0)

    def get_solution(self):
        return self.best_solution

    def print_solution(self):
        print("Best Solution:")
        for i in range(self.num_vertices):
            print(f"Vertex {i + 1} is colored with color {self.color_names[self.best_solution[i]]}")  # Use color names


# Example usage:
if __name__ == "__main__":
   
    # graph = [
    #     [0, 1, 1, 0, 1],
    #     [1, 0, 1, 0, 1],
    #     [1, 1, 0, 1, 0],
    #     [0, 0, 1, 0, 1],
    #     [1, 1, 0, 1, 0]
    # ]
    graph = [
        [0,1,0,0,0],
        [0,0,1,1,0],
        [0,0,0,0,1],
        [0,1,0,0,0],
        [1,0,0,1,0]
    ]
    
    num_colors = 3  # Number of colors available

    color_names = ["Red", "Blue", "Green"]  # Define color names

    coloring_problem = GraphColoring(graph, num_colors, color_names)  # Pass color names
    coloring_problem.branch_and_bound()
    coloring_problem.print_solution()

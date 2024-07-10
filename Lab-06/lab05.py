import heapq

def a_star_search(graph, heuristics, start, goal):
    # Priority queue for nodes to explore
    open_list = []
    heapq.heappush(open_list, (heuristics[start], 0, start, []))
    
    # Dictionary for visited nodes with the cost to reach them
    closed_list = {}
    
    while open_list:
        # Pop the node with the lowest f = g + h
        f, g, current_node, path = heapq.heappop(open_list)
        
        # If the goal is reached, return the path
        if current_node == goal:
            return path + [current_node]
        
        # If the current node is already visited with a lower cost, skip it
        if current_node in closed_list and closed_list[current_node] <= g:
            continue
        
        # Record the cost to reach the current node
        closed_list[current_node] = g
        
        # Explore neighbors
        for neighbor, weight in graph[current_node]:
            new_g = g + weight
            new_f = new_g + heuristics[neighbor]
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [current_node]))
    
    # Return an empty path if no path is found
    return []

# Define the graph as an adjacency list based on the image
graph = {
    'A': [('B', 6), ('F', 3)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1)],
    'D': [('B', 2), ('C', 1), ('E', 5)],
    'E': [('D', 5), ('J', 3)],
    'F': [('A', 3), ('G', 1)],
    'G': [('F', 1), ('I', 2)],
    'H': [('I', 2)],
    'I': [('G', 2), ('H', 2), ('J', 1)],
    'J': [('E', 3), ('I', 1)]
}

# Define the heuristic values for each node based on the image
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

# Perform the A* search
start = 'A'
goal = 'J'
path = a_star_search(graph, heuristics, start, goal)

print(f"The most cost-effective path from {start} to {goal} is: {path}")

from collections import deque

# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS traversal function
def bfs(graph,start):
    visited=set()
    queue=deque([start])

    while queue:
        node=queue.popleft()
    
        if node in visited:
            continue

        visited.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)


# Run BFS from node 'A'
bfs(graph, 'A')

def dfs(graph,start,visited=None):

    if visited is None:
        visited=set()
    
    visited.add(start)

    for neighbours in graph[start]:
        if neighbours not in visited:
            dfs(graph,neighbours,visited)
        
    
    return visited


if __name__=="__main__":
    graph= {
        'A': ['B','C'],
        'B': ['A','D'],
        'C': ['A', 'E', 'F'],
        'D': ['B'],
        'E': ['C'],
        'F': ['C']
    }

    print("Graph Structure")

    for node,neighbours in graph.items():
        print(f"{node} -> {neighbours}")
    
    print("DFS")
    visited_nodes=dfs(graph,'A')
    print(f"\nAll visited nodes: {visited_nodes}")
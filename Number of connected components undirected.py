from collections import defaultdict
# Brute Force TC: O(nodes+edges)
def count_components(n,edges):
#     graph=defaultdict(list)

#     for u,v in edges:
#         graph[u].append(v)
#         graph[v].append(u)

#     visited=set()
#     count=0

#     def dfs(node):
#         for neighbour in graph[node]:
#             if neighbour not in visited:
#                 visited.add(neighbour)
#                 dfs(neighbour)
    
#     for node in range(n):
#         if node not in visited:
#             visited.add(node)
#             dfs(node)
#             count+=1

# edges=[[0,1],[1,2],[3,4]]
# count_components(5,edges)
    par=[i for i in range(n)]
    rank= [1]* n

    def find(n1):
        res=n1

        while res != par[res]:
            par[res] = par[par[res]]
            res=par[res]
        return res
    
    def union(n1,n2):
        p1,p2= find(n1), find(n2)

        if p1==p2:
            return 0
        
        if rank[p2]> rank[p1]:
            par[p1] = p2
            rank[p2] += rank[p1]

        else:
            par[p2] = p1
            rank[p1] += rank[p2]
        
        return 1

    res=n
    for n1, n2 in edges:
        res -= union(n1,n2)
        
    return res
        
edges=[[0,1],[1,2],[3,4]]




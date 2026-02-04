# Week 03 - Graph Reachability and Components
# Jonathan (Johnny) McKinnon

def reachability(s: int, G: list[list[int]]) -> list[int]:
    """
    Returns a list of all vertices reachable from vertex [s] in graph [G]
    int s-Starting vertex 
    G(List[List[int]]): Adjacency matrix of the graph

    Returns:
        List[int]: List of reachable vertices
        0=not connected, 1=connected
    """
    #reuses DFS algorithm to find all reachable vertices from s in entire graph G
    visited = [False] * len(G)   # Identifes visited vertices
    stack = [s]                 # Stack for Depth-First Search
    reachable = [] # stores final answer - vertices reachable from s

    while stack:
        v = stack.pop() # return/remove last element of stack [0, 0, 1]-1

        if not visited[v]:
            visited[v] = True # ensures no duplicates nodes are visited
            reachable.append(v) # add vertex to final result list

            # Add all neighbors to the stack
            for neighbor, edge in enumerate(G[v]): # (index, value)
                if edge == 1 and not visited[neighbor]: # (locates next node)
                    stack.append(neighbor) # add neighbor to stack

    return reachable

def count_components(G: list[list[int]]) -> int:
    """
    Counts number of connected components in graph G.
    Returns - Number of components(int value).
    """

    visited = [False] * len(G)
    components = 0

    for vertex in range(len(G)):
        if not visited[vertex]: # finds unvisited vertex = must be a new component
            stack = [vertex] # start DFS from this specified vertex

            while stack:
                v = stack.pop() #return/remove last element of stack

                if not visited[v]: 
                    visited[v] = True

                    for neighbor, edge in enumerate(G[v]): # (index, value)
                        if edge == 1 and not visited[neighbor]: # locates next node
                            stack.append(neighbor)

            components += 1

    return components

# Test graph - represented as adjacency matrix in time complexity O(n^2)
# n=number of vertices connected by edges
graph = [
    # 0  1  2  3  4  5  6  7
    [ 0, 0, 0, 1, 0, 0, 1, 0],  # vertex 0
    [ 0, 0, 0, 0, 0, 1, 0, 0],  # vertex 1
    [ 0, 0, 0, 0, 1, 0, 0, 0],  # vertex 2
    [ 1, 0, 0, 0, 0, 1, 0, 0],  # vertex 3
    [ 0, 0, 1, 0, 0, 0, 0, 0],  # vertex 4
    [ 0, 1, 0, 1, 0, 0, 0, 0],  # vertex 5
    [ 1, 0, 0, 0, 0, 0, 0, 0],  # vertex 6
    [ 0, 0, 0, 0, 0, 0, 0, 0]   # vertex 7
] # columns and rows represent vertices: LEGEND - 1=connected, 0=not connected

print(reachability(3, graph))
print(count_components(graph))
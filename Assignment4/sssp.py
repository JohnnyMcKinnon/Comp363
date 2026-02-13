# Johnny McKinnon
# Assignment 4 – DAG Shortest Paths
# COMP363

from typing import List, Optional


def sssp(source: int, graph: List[List[int]]) -> List[float]:
    """
    Finds the shortest distance from the source vertex to every
    other vertex using edge relaxation.
    """

    # Sanity check
    if not graph:
        raise ValueError("Graph cannot be empty.")

    n = len(graph)

    # 0 = no edge
    no_edge = graph[0][0]

    infinity = float("inf")

    # Assume each vertex is infinite distance
    distances = [infinity] * n
    distances[source] = 0  # [0,0]

    # Keeps track of vertices that still need processing
    stack = [source]

    while stack:
        u = stack.pop()  # grab the next vertex to relax edges from

        # Checks all possible neighbors
        for v in range(n):

            # Skip if 0 [no edge]
            if graph[u][v] != no_edge:

                new_distance = distances[u] + graph[u][v]

                # If shorter path found, update
                if new_distance < distances[v]:
                    distances[v] = new_distance

                    # Since v improved, recheck neighbors
                    stack.append(v)

    return distances


def reconstruct(
    distances: List[float],
    source: int,
    graph: List[List[int]]
) -> List[Optional[int]]:
    # Builds a predecessor list to recover actual shortest paths after computing
    #distances

    n = len(graph)
    no_edge = graph[0][0]

    # None means a vertex has no predecessor (true for source)
    predecessors: List[Optional[int]] = [None] * n

    for v in range(n):

        # Source has no parent in path
        if v == source:
            continue

        # vertex[u] leads to [v] optimally
        for u in range(n):

            if graph[u][v] != no_edge:

                # If pass, edge is already part of a shortest path
                if distances[u] + graph[u][v] == distances[v]:
                    predecessors[v] = u
                    break  # stop once correct predecessor is found

    return predecessors


def report_sssp(
    predecessors: List[Optional[int]],
    distances: List[float],
    graph: List[List[int]]
) -> None:
    # Prints each shortest path in order from source + total distance.

    for vertex in range(len(graph)):

        # If still infinity, vertex was never reached
        if distances[vertex] == float("inf"):
            print(f"Vertex {vertex}: No path")
            continue

        path = []
        current = vertex

        # traverse backwards through predecessors until source
        while current is not None:
            path.append(current)
            current = predecessors[current]

        # Reverse to print from source -> destination
        path.reverse()

        print(f"Vertex {vertex}: {' -> '.join(map(str, path))} | Distance = {distances[vertex]}")
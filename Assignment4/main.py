# Johnny McKinnon
# COMP363
# Assignment 4- SSSP-dag


from sssp import sssp, reconstruct, report_sssp

def main():
    # Build sample directed acyclic graph (DAG)
    # run shortest path algorithm from source vertex, then prints resulting paths

    # Adjacency matrix representation of graph
    # Value 0 = no directed edge.
    graph = [
    #    0   1   2   3   4   5   6   7
        [0,  5,  1,  5, 10,  0,  0,  0],  # 0
        [0,  0, 12,  5,  6,  0,  0,  0],  # 1
        [0,  0,  0,  1,  0,  0,  5,  0],  # 2
        [0,  0,  0,  0,  0,  1,  5,  0],  # 3
        [0,  0,  0,  6,  0,  5,  0,  5],  # 4
        [0,  0,  0,  0,  0,  0,  1,  5],  # 5
        [0,  0,  0,  0,  0,  0,  0,  1],  # 6
        [0,  0,  0,  0,  0,  0,  0,  0],  # 7
    ]

    # Starting vertex
    # Changing value will recompute paths from new source
    source_vertex = 0

    print(f"\nRunning SSSP starting from vertex {source_vertex}...\n")

    # Step 1: Compute shortest distances from source
    distances = sssp(source_vertex, graph)

    # Step 2: Reconstruct predecessor list to recover paths
    predecessors = reconstruct(distances, source_vertex, graph)

    # Step 3: Display final shortest paths
    report_sssp(predecessors, distances, graph)


# Confirms main() runs when file is executed directly
if __name__ == "__main__":
    main()
def dijkstra(n, source, cost):
    v = [0] * (n + 2)
    d = [float('inf')] * (n + 2)
    p = [[] for _ in range(n + 2)]

    d[source] = 0
    p[source] = [source]

    for _ in range(n):
        u = min((i for i in range(1, n + 1) if not v[i]), key=lambda i: d[i])
        v[u] = 1

        for w in range(1, n + 1):
            if not v[w]:
                x = d[u] + cost[u][w]
                if x < d[w]:
                    d[w] = x
                    p[w] = p[u] + [w]

    return d, p

def main():
    n = int(input("Vertices: "))
    cost = [[float('inf')] * (n + 2) for _ in range(n + 2)]

    for i in range(1, n + 1):
        cost[i][1:n + 1] = map(int, input(f"Costs for vertex {i}: ").split())

    source = int(input("Source vertex: "))
    distances, shortest_paths = dijkstra(n, source, cost)

    print(f"Shortest paths from {source}:")
    for i in range(1, n + 1):
        if i != source:
            print(f"{source} -> {' -> '.join(map(str, shortest_paths[i][1:]))} = {distances[i]}")

if __name__ == "__main__":
    main()
# dijkstra: The name of the algorithm.
# num_vertices: The number of vertices in the graph.
# source_vertex: The starting vertex for finding shortest paths.
# edge_costs: The costs or weights of edges in the graph.
# visited: A list to keep track of visited vertices.
# distances: A list to store the shortest distances from the source to each vertex.
# paths: A list to store the shortest paths from the source to each vertex.
# current_vertex: The current vertex being processed in the algorithm.
# neighbor_vertex: A vertex adjacent to the current vertex.
# potential_distance: The potential new distance for a neighbor vertex.

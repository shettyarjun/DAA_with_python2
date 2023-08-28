def dijkstra(n, source, cost):
    visited = [False] * (n + 2)
    distance = [float('inf')] * (n + 2)
    path = [[] for _ in range(n + 2)]
    
    distance[source] = 0
    path[source] = [source]
    
    for _ in range(n):
        # Find the unvisited vertex with the smallest distance
        u = min((i for i in range(1, n + 1) if not visited[i]), key=lambda i: distance[i])
        visited[u] = True
        
        # Update distances and paths
        for w in range(1, n + 1):
            if not visited[w] and (d := distance[u] + cost[u][w]) < distance[w]:
                distance[w], path[w] = d, path[u] + [w]
    
    return distance, path

def main():
    n = int(input("Enter the number of vertices: "))
    cost = [[float('inf')] * (n + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        cost[i][1:n + 1] = map(int, input(f"Enter costs for vertex {i}: ").split())

    source = int(input("Enter the source vertex: "))
    distances, shortest_paths = dijkstra(n, source, cost)

    print(f"Shortest paths from source {source} to the remaining vertices:")
    for i in range(1, n + 1):
        if i != source:
            print(f"{source} -> {' -> '.join(map(str, shortest_paths[i][1:]))} = {distances[i]}")

if __name__ == "__main__":
    main()

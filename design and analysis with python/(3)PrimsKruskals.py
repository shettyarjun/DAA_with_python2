def Prims(n, cost):
    selected = [0] * n  # Keeps track of selected vertices
    selected[0] = 1
    
    for _ in range(n - 1):
        minimum, x, y = float('inf'), 0, 0
        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j] < minimum:
                        minimum, x, y = cost[i][j], i, j
        print(x + 1, '-->', y + 1, ':', minimum)  # Print selected edge
        selected[y] = 1

def Kruskals(n, cost):
    parent = list(range(n))  # Initialize each vertex as its own parent
    edges = [(i, j, cost[i][j]) for i in range(n) for j in range(i + 1, n) if cost[i][j] > 0]
    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    
    mincost = 0
    for a, b, weight in edges:
        if parent[a] != parent[b]:  # Check if adding the edge forms a cycle
            mincost += weight
            print("Edge:", a + 1, "-->", b + 1, "cost:", weight)  # Print selected edge
            parent = [parent[b] if p == parent[a] else p for p in parent]
    
    print("Minimum cost =", mincost)

def main():
    n = int(input("Enter the number of nodes: "))
    cost = [list(map(int, input().split())) for _ in range(n)]

    print("Minimum Spanning Tree using Prim's Algorithm:")
    Prims(n, cost)

    print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
    Kruskals(n, cost)

if __name__ == "__main__":
    main()

def prims_mst(n, cost):
    selected, mincost = [0], 0
    print("Minimum Spanning Tree Edges using Prim's Algorithm:")
    for _ in range(n - 1):
        x, y, minimum = 0, 0, float('inf')
        for i in selected:
            for j in range(n):
                if j not in selected and cost[i][j] < minimum:
                    x, y, minimum = i, j, cost[i][j]
        selected.append(y)
        mincost += minimum
        print(f"Edge: {x + 1} --> {y + 1} : Cost = {minimum}")
    print("Minimum Cost using Prim's Algorithm:", mincost)

def kruskals_mst(n, cost):
    edges = sorted((cost[i][j], i, j) for i in range(n) for j in range(i + 1, n) if cost[i][j])
    parent, mincost = list(range(n)), 0
    print("\nMinimum Spanning Tree Edges using Kruskal's Algorithm:")
    for weight, a, b in edges:
        if parent[a] != parent[b]:
            mincost += weight
            print(f"Edge: {a + 1} --> {b + 1} : Cost = {weight}")
            parent = [parent[b] if p == parent[a] else p for p in parent]
    print("Minimum Cost using Kruskal's Algorithm:", mincost)

def main():
    n = int(input("Enter the number of nodes: "))
    cost = [list(map(int, input().split())) for _ in range(n)]
    prims_mst(n, cost)
    kruskals_mst(n, cost)

if __name__ == "__main__":
    main()

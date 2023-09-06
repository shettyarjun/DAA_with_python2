maxi = 9999999
n = int(input("Enter the number of nodes: "))

def prim_mst(n, cost):
    selected = [False] * n
    selected[0] = True

    for _ in range(n - 1):
        minimum = maxi
        x = y = 0

        for i in range(n):
            if selected[i]:
                for j in range(n):
                    if not selected[j] and cost[i][j] and cost[i][j] < minimum:
                        minimum = cost[i][j]
                        x = i
                        y = j

        print(x, '-->', y, ':', cost[x][y])
        selected[y] = True

def kruskal_mst(n, cost):
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            if cost[i][j]:
                edges.append((i, j, cost[i][j]))

    edges.sort(key=lambda x: x[2])
    parent = list(range(n))

    mincost = 0
    for edge in edges:
        a, b, weight = edge
        if parent[a] != parent[b]:
            mincost += weight
            print("Edge:", a, '-->', b, ':', weight)
            old_parent = parent[a]
            new_parent = parent[b]
            for i in range(n):
                if parent[i] == old_parent:
                    parent[i] = new_parent

    print("Minimum cost =", mincost)

cost = [[int(x) for x in input().split()] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if cost[i][j] == 0:
            cost[i][j] = maxi

print("Minimum Spanning Tree using Prim's Algorithm:")
prim_mst(n, cost)
print("\nMinimum Spanning Tree using Kruskal's Algorithm:")
kruskal_mst(n, cost)

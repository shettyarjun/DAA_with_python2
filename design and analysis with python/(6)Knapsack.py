def knapsack_solve(wt, val, W, N):
    sol = [[0 for _ in range(W + 1)] for _ in range(N + 1)]
    selected = [0] * (N + 1)
    
    for i in range(1, N + 1):
        for j in range(1, W + 1):
            if wt[i] > j:
                sol[i][j] = sol[i - 1][j]
            else:
                sol[i][j] = max(sol[i - 1][j], sol[i - 1][j - wt[i]] + val[i])

    print("The optimal solution is:", sol[N][W])
    i, j = N, W

    while i > 0 and j > 0:
        if sol[i][j] != sol[i - 1][j]:
            selected[i] = 1
            j -= wt[i]
        i -= 1

    print("\nItems selected:")
    for i in range(1, N + 1):
        if selected[i] == 1:
            print(i, end=" ")
    print()

def main():
    n = int(input("Enter number of elements: "))
    wt = [0] * (n + 1)
    val = [0] * (n + 1)

    print("\nEnter weight of", n, "elements (separated by spaces):")
    wt_input = input().split()
    for i in range(1, n + 1):
        wt[i] = int(wt_input[i - 1])

    print("\nEnter values of", n, "elements (separated by spaces):")
    val_input = input().split()
    for i in range(1, n + 1):
        val[i] = int(val_input[i - 1])

    W = int(input("\nEnter knapsack capacity: "))
    knapsack_solve(wt, val, W, n)

if __name__ == "__main__":
    main()

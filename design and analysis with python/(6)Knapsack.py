def knapsack_solve(weights, values, capacity, N):
    dp = [[0] * (capacity + 1) for _ in range(N + 1)]
    
    # Fill the dynamic programming table
    for i in range(1, N + 1):
        for w in range(1, capacity + 1):
            if weights[i] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i] + dp[i - 1][w - weights[i]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtrack to find the selected items
    selected = []
    i, w = N, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i)
            w -= weights[i]
        i -= 1

    return dp[N][capacity], selected[::-1]  # Reversing to get the correct sequence

def main():
    n = int(input("Enter number of items: "))
    weights = [0] + list(map(int, input("Enter weights of items: ").split()))
    values = [0] + list(map(int, input("Enter values of items: ").split()))
    capacity = int(input("Enter knapsack capacity: "))
    
    optimal_value, selected_items = knapsack_solve(weights, values, capacity, n)

    print("Optimal value:", optimal_value)
    print("Selected items:", " ".join(map(str, selected_items)))

if __name__ == "__main__":
    main()

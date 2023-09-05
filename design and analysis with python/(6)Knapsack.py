def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    optimal_value = dp[n][capacity]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]
        i -= 1

    selected_items.reverse()

    return optimal_value, selected_items

def main():
    n = int(input("Enter number of items: "))
    weights = list(map(int, input("Enter weights of items: ").split()))
    values = list(map(int, input("Enter values of items: ").split()))
    capacity = int(input("Enter knapsack capacity: "))
    
    optimal_value, selected_items = knapsack(weights, values, capacity)

    print("Optimal value:", optimal_value)
    print("Selected items:", " ".join(map(str, selected_items)))

if __name__ == "__main__":
    main()

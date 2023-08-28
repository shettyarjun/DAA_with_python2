class Sales:
    def __init__(self):
        self.cost, self.memo = [], []
    
    def dp(self, city, n, mask):
        if mask == (1 << n) - 1:
            return self.cost[city][0]
        if self.memo[city][mask] != -1:
            return self.memo[city][mask]
        ans = float('inf')
        for i in range(n):
            if not (mask & (1 << i)) and self.cost[city][i]:
                ans = min(ans, self.cost[city][i] + self.dp(i, n, mask | (1 << i)))
        self.memo[city][mask] = ans
        return ans
    
    def path(self, city, n, mask):
        if mask == (1 << n) - 1:
            return [city, 0]
        next_city, min_cost = -1, float('inf')
        for i in range(n):
            if not (mask & (1 << i)) and self.cost[city][i]:
                cost = self.cost[city][i] + self.dp(i, n, mask | (1 << i))
                if cost < min_cost:
                    min_cost, next_city = cost, i
        return [city] + self.path(next_city, n, mask | (1 << next_city))
    
    def solve(self, n):
        self.memo = [[-1] * (1 << n) for _ in range(n)]
        optimal_cost = self.dp(0, n, 1)
        optimal_path = self.path(0, n, 1)
        return optimal_cost, optimal_path
    
def main():
    x = Sales()
    n = int(input())
    x.cost = [list(map(int, input().split())) for _ in range(n)]
    cost, path = x.solve(n)
    print("Path:", " -> ".join(map(str, path)))
    print("Cost:", cost)

if __name__ == "__main__":
    main()

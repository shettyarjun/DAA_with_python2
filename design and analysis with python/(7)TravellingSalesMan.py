class Sales:
    def __init__(self, n):
        self.n = n
        self.cost_opt = 0
        self.a = [[0] * n for _ in range(n)]
        self.visit = [0] * n

    def mincost_opt(self, city):
        self.visit[city] = 1
        print(city, "-->", end=" ")
        ncity = self.least_opt(city)
        if ncity == 999:
            ncity = 1
            print(ncity)
            self.cost_opt += self.a[city][ncity]
            return
        self.mincost_opt(ncity)

    def least_opt(self, c):
        nc = 999
        min_val = 999
        kmin = 999
        for i in range(1, self.n):
            if self.a[c][i] != 0 and self.visit[i] == 0:
                if self.a[c][i] < min_val:
                    min_val = self.a[c][i]
                    kmin = self.a[c][i]
                    nc = i
        if min_val != 999:
            self.cost_opt += kmin
        return nc

def main():
    n = int(input("Enter the number of cities: "))
    x = Sales(n + 1)  # Added +1 to accommodate the extra element
    print("Enter the cost matrix:")
    for i in range(1, n + 1):  # Changed the loop range to n+1
        row = list(map(int, input().split()))
        for j in range(1, n + 1):  # Changed the loop range to n+1
            x.a[i][j] = row[j - 1]
            x.visit[i] = 0
  
    print("Optimal solution:")
    print("The path is:")
    x.mincost_opt(1)
    print("Minimum cost is", x.cost_opt)

if __name__ == "__main__":
    main()

inf = float('inf')

class TSP:
    def __init__(self):
        self.n = 0
        self.matrix = []

    def get_input(self):
        self.n = int(input("Enter number of cities: "))
        self.matrix = []

        print("Enter distance matrix row by row:")
        for _ in range(self.n):
            row = list(map(int, input().split()))
            self.matrix.append(row)

    def nearest_neighbor(self, start):
        visited = [False] * self.n
        path = [start]
        cost = 0

        current = start
        visited[start] = True

        for _ in range(self.n - 1):
            next_city = -1
            min_dist = inf

            for j in range(self.n):
                if not visited[j] and self.matrix[current][j] < min_dist:
                    min_dist = self.matrix[current][j]
                    next_city = j

            if next_city == -1:
                return [], inf

            visited[next_city] = True
            path.append(next_city)
            cost += min_dist
            current = next_city

        cost += self.matrix[current][start]
        path.append(start)

        return path, cost

    def solve(self):
        best_cost = inf
        best_path = []

        for start in range(self.n):
            path, cost = self.nearest_neighbor(start)

            print(f"Start {start} → Path: {path}, Cost: {cost}")

            if cost < best_cost:
                best_cost = cost
                best_path = path

        print("\nBest Tour:", best_path)
        print("Minimum Cost:", best_cost)


tsp = TSP()
tsp.get_input()
tsp.solve()


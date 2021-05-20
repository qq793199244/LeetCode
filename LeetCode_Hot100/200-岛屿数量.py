'''
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
示例 1：
输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：
输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
'''


class Solution:
    # DFS。时间复杂度O(mn)，空间复杂度O(mn)
    def numIslands1(self, grid):
        m, n, count = len(grid), len(grid[0]), 0

        def dfs(row, col):
            # 注意边界条件
            if not 0 <= row < m or not 0 <= col < n or grid[row][col] != '1':
                return
            # 已访问过的标记为'2'
            grid[row][col] = '2'
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

    # BFS。时间复杂度O(mn)，空间复杂度O(min(m, n))
    def numIslands2(self, grid):
        m, n, count = len(grid), len(grid[0]), 0

        def bfs(i, j):
            queue = [(i, j)]
            grid[i][j] = "2"
            while queue:
                x, y = queue.pop(0)
                for r, c in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                        queue.append((r, c))
                        grid[r][c] = "2"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count

    # 并查集。时间复杂度O(mn*α(mn))，空间复杂度O(mn)
    def numIslands3(self, grid):
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        uf = UnionFind(grid)
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    grid[r][c] = "0"
                    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "1":
                            uf.union(r * nc + c, x * nc + y)
        return uf.getCount()


class UnionFind:
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [0] * (m * n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] < self.rank[rooty]:
                rootx, rooty = rooty, rootx
            self.parent[rooty] = rootx
            if self.rank[rootx] == self.rank[rooty]:
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


if __name__ == '__main__':
    u = Solution()
    grid1 = [["1", "1", "1", "1", "0"],
             ["1", "1", "0", "1", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "0", "0", "0"]]
    grid2 = [["1", "1", "0", "0", "0"],
             ["1", "1", "0", "0", "0"],
             ["0", "0", "1", "0", "0"],
             ["0", "0", "0", "1", "1"]]
    grid3 = [["1"]]
    grid4 = [["0"]]
    grid5 = [[]]

    # print(u.numIslands1(grid1))
    # print(u.numIslands1(grid2))
    # print(u.numIslands1(grid3))
    # print(u.numIslands1(grid4))
    # print(u.numIslands1(grid5))

    # print(u.numIslands2(grid1))
    # print(u.numIslands2(grid2))
    # print(u.numIslands2(grid3))
    # print(u.numIslands2(grid4))
    # print(u.numIslands2(grid5))

    print(u.numIslands3(grid1))
    print(u.numIslands3(grid2))
    print(u.numIslands3(grid3))
    print(u.numIslands3(grid4))
    print(u.numIslands3(grid5))

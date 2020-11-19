'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
'''
class Solution(object):
    def minPathSum(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[0][j]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j] + grid[i][0]
                else:
                    dp[i][j] += min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
        return dp[-1][-1]
# 时间复杂度O(mn)
# 空间复杂度O(mn)

if __name__ == '__main__':
    u = Solution()
    g = [[1, 2, 3, 4, 5]]
    print(u.minPathSum(g))
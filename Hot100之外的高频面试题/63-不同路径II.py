'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
示例 1：
输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：
输入：obstacleGrid = [[0,1],[0,0]]
输出：1
'''


class Solution(object):
    # 动态规划。时间复杂度O(m*n)，空间复杂度O(m*n)
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m * n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        if dp[0][0] == 0:
            return 0
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] != 1:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    u = Solution()
    print(u.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))  # 2
    print(u.uniquePathsWithObstacles([[0, 1], [0, 0]]))  # 1

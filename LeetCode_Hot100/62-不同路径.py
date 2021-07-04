'''
一个机器人位于一个 m x n网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
示例 1：
输入：m = 3, n = 7     输出：28
示例 2：
输入：m = 3, n = 2     输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 3：
输入：m = 7, n = 3     输出：28
示例 4：
输入：m = 3, n = 3     输出：6
提示：
1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
'''


class Solution:
    # 暴力递归，会超时。时间复杂度O(2^(m + n - 1) - 1)
    def uniquePaths(self, m, n):
        def dfs(i, j):
            if i == 0 or j == 0:
                return 1
            return dfs(i - 1, j) + dfs(i, j - 1)
        return dfs(m - 1, n - 1)

    # 动态规划；时间复杂度O(m * n)，空间复杂度O(m * n)
    def uniquePaths2(self, m, n):
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 只有一行或只有一列
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # 动态规划优化；时间复杂度O(m * n)，空间复杂度O(n)
    '''
    dp[j] += dp[j-1] 即 dp[j] = dp[j-1] + dp[j] 
    未赋值之前右边的dp[j]始终表示当前行第i行的上一行第j列的值，
    赋值之后左边的dp[j]表示当前行第i行第j列的值，dp[j-1]表示当前行第i行第j-1列的值
    (dp[j-1] 在计算dp[j]之前就已经计算了，所以表示的是当前行而不是上一行)
    '''

    def uniquePaths3(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == '__main__':
    u = Solution()
    print(u.uniquePaths(3, 7))  # 28
    print(u.uniquePaths(3, 2))  # 3
    print(u.uniquePaths(7, 3))  # 28
    print(u.uniquePaths(3, 3))  # 6

    print('--------------------')
    print(u.uniquePaths2(3, 7))  # 28
    print(u.uniquePaths2(3, 2))  # 3
    print(u.uniquePaths2(7, 3))  # 28
    print(u.uniquePaths2(3, 3))  # 6

    print('--------------------')
    print(u.uniquePaths3(3, 7))  # 28
    print(u.uniquePaths3(3, 2))  # 3
    print(u.uniquePaths3(7, 3))  # 28
    print(u.uniquePaths3(3, 3))  # 6

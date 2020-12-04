'''
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
'''

class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        res = 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if (matrix[i - 1][j - 1] == '1'):
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                    res = max(dp[i][j], res)
        return res * res


if __name__ == '__main__':
    u = Solution()
    m = [['0', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1'],
        ['1', '0', '1', '1', '1'],
        ['0', '0', '0', '1', '1'],
        ['0', '0', '0', '1', '0']]
    print(u.maximalSquare(m))

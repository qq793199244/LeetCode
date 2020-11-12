'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
问总共有多少条不同的路径？
'''

class Solution(object):
    def uniquePaths(self, m, n):
        f = [[1]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]
        return f[-1][-1]


if __name__ == '__main__':
    u = Solution()
    m = 7
    n = 3
    res = u.uniquePaths(m, n)
    print(res)
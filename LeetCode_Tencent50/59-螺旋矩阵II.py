'''
给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
示例 1：
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：
输入：n = 1
输出：[[1]]
提示：
1 <= n <= 20
'''


class Solution:
    # 同LeetCode54，多了数组初始化这一步。时间复杂度O(n^2)，空间复杂度O(n^2)，如果输出结果不算空间则为O(1)
    def generateMatrix(self, n):
        if n == 0:
            return []
        # 初始化数组
        res = [[0 for _ in range(n)] for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num, tar = 1, n * n
        while num <= tar:
            while left <= right and top <= bottom:
                for col in range(left, right + 1):
                    res[top][col] = num
                    num += 1
                for row in range(top + 1, bottom + 1):
                    res[row][right] = num
                    num += 1
                if left < right and top < bottom:
                    for col in range(right - 1, left - 1, -1):
                        res[bottom][col] = num
                        num += 1
                    for row in range(bottom - 1, top, -1):
                        res[row][left] = num
                        num += 1
                left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.generateMatrix(3))  # [[1,2,3],[8,9,4],[7,6,5]]
    print(u.generateMatrix(1))  # [[1]]
    print(u.generateMatrix(0))  # []

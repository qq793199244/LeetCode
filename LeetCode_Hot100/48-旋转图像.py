'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''


class Solution:
    # 不符合题目要求的方法
    # 占用额外空间。时间复杂度O(n^2)，空间复杂度O(n^2)
    # 发现规律：行坐标i → 列坐标；列坐标 → n-1-i
    def rotate(self, matrix):
        if not matrix and not matrix[0] and len(matrix) != len(matrix[0]):
            return
        n = len(matrix)
        new_matrix = [[0 for _ in range(n)] for _ in range(n)]
        for col in range(n):
            for row in range(n):
                new_matrix[col][n - 1 - row] = matrix[row][col]
        return new_matrix

    # 原地旋转。时间复杂度O(n^2)，空间复杂度O(1)
    def rotate2(self, matrix):
        if not matrix and not matrix[0] and len(matrix) != len(matrix[0]):
            return
        n = len(matrix)
        for row in range(n // 2):
            for col in range((n + 1) // 2):
                matrix[row][col], matrix[n - col - 1][row], \
                matrix[n - row - 1][n - col - 1], matrix[col][n - row - 1] \
                    = matrix[n - col - 1][row], matrix[n - row - 1][n - col - 1], \
                      matrix[col][n - row - 1], matrix[row][col]
        return matrix

    # 原地，用翻转代替旋转。时间复杂度O(n^2)，空间复杂度O(1)
    def rotate3(self, matrix):
        if not matrix and not matrix[0] and len(matrix) != len(matrix[0]):
            return
        n = len(matrix)
        # 转置
        for row in range(n):
            for col in range(row, n):
                matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
        # 每行逆序，翻转
        for r in range(n):
            matrix[r].reverse()
        return matrix


if __name__ == '__main__':
    u = Solution()
    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    m2 = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]]
    print(u.rotate(m1))
    print(u.rotate(m2))

    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    m2 = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]]
    print(u.rotate2(m1))
    print(u.rotate2(m2))

    m1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
    m2 = [[5, 1, 9, 11],
          [2, 4, 8, 10],
          [13, 3, 6, 7],
          [15, 14, 12, 16]]
    print(u.rotate3(m1))
    print(u.rotate3(m2))


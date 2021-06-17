'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
示例 1：
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    # 按层打印。时间复杂度O(mn)，空间复杂度O(mn)，如果返回结果不算空间，则是O(1)
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        left, right, top, bottom = 0, n - 1, 0, m - 1
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


if __name__ == '__main__':
    u = Solution()
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    m3 = []
    m4 = [[1]]
    print(u.spiralOrder(m1))
    print(u.spiralOrder(m2))
    print(u.spiralOrder(m3))
    print(u.spiralOrder(m4))

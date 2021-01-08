'''
给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
示例:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出:  [1,2,4,7,5,3,6,8,9]
说明:
给定矩阵中的元素总数不会超过 100000 。
'''


class Solution:
    # 模拟；时间复杂度O(m*n)，空间复杂度O(1)，输出res数组不算占用额外空间
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0, 0
        turn = 1  # turn转向变量，turn=1为右上方向，turn=-1为左下方向
        total = m * n  # 元素总数
        res = []
        while total:
            while 0 <= i < m and 0 <= j < n:  # 边界，当超出上边界和左边界时跳出循环
                res.append(matrix[i][j])
                total -= 1
                i -= turn
                j += turn
            if turn == 1:  # 右上方向↗，关心右边届和上边界，要先判断右边届
                if j == n:  # j超右界情况，i该往下移2次，同时j恢复列最大值n-1
                    i += 2
                    j = n - 1
                else:  # i超上界，i置0 （思考问什么不把上边界放前面？当遍历到右上角的右上时，i先置0会影响后面赋值）
                    i = 0
            else:  # 左下方向↙，关心下边界和左边届，要先判断下边界（左下角）
                if i == m:  # i超下界，j该往右移2次，同时i恢复行最大值
                    j += 2
                    i = m - 1
                else:  # j超左界，j置0
                    j = 0
            turn *= -1  # 改变方向
        return res

    def findDiagonalOrder2(self, matrix):
        if not matrix or not matrix[0]:
            return []
        rows, cols, res, count = len(matrix), len(matrix[0]), [], 0
        for count in range(1, cols + rows):
            i = 0 if count <= cols else count - cols
            j = count - 1 if count <= cols else cols - 1
            temp_list = []
            while 0 <= i < rows and 0 <= j < cols:
                temp_list.append(matrix[i][j])
                i += 1
                j -= 1
            if count % 2 == 0:
                res += temp_list
            else:
                res += temp_list[::-1]
        return res


if __name__ == '__main__':
    u = Solution()
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]  # [1,2,4,7,5,3,6,8,9]

    m2 = [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]  # [1,2,3,5,4,6,7,8]
    m3 = [[1, 2, 3, 4, 5, 6, 7]]  # [1,2,3,4,5,6,7]
    m4 = [
        [1],
        [2],
        [3],
        [4]
    ]  # [1,2,3,4]
    m5 = []  # []
    print(u.findDiagonalOrder(m1))
    print(u.findDiagonalOrder(m2))
    print(u.findDiagonalOrder(m3))
    print(u.findDiagonalOrder(m4))
    print(u.findDiagonalOrder(m5))

    print(u.findDiagonalOrder2(m1))
    print(u.findDiagonalOrder2(m2))
    print(u.findDiagonalOrder2(m3))
    print(u.findDiagonalOrder2(m4))
    print(u.findDiagonalOrder2(m5))

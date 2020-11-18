'''
给定一个含有 M x N 个元素的矩阵（M 行，N 列），
请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
示例:
输入:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
输出:  [1,2,4,7,5,3,6,8,9]
'''
class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])  # 边界
        i, j, turn = 0, 0, 1  # turn转向变量
        total = m * n
        res = []
        while total:
            while 0 <= i < m and 0 <= j < n:
                res.append(matrix[i][j])
                total -= 1
                i -= turn
                j += turn
            if turn == 1:
                if j == n:  # j超右界，i该往下移2次，同时j恢复列最大值
                    i += 2
                    j = n - 1
                else:  # i超上界，i置0
                    i = 0
            else:
                if i == m:  # i超下界，j该往右移2次，同时i恢复行最大值
                    j += 2
                    i = m - 1
                else:  # j超左界，j置0
                    j = 0
            turn *= -1
        return res
# 时间复杂度O(mn)
# 空间复杂度O(1)
        

if __name__ == '__main__':
    u = Solution()
    m1 = [[ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]]
    m2 = []
    m3 = [[1, 2, 3, 4]]
    m4 = [[1],
          [2],
          [3],
          [4]]
    print(u.findDiagonalOrder(m1))
    print(u.findDiagonalOrder(m2))
    print(u.findDiagonalOrder(m3))
    print(u.findDiagonalOrder(m4))
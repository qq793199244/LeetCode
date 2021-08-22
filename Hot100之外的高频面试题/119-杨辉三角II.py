'''
给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
在「杨辉三角」中，每个数是它左上方和右上方的数的和。
示例 1:
输入: rowIndex = 3
输出: [1,3,3,1]
示例 2:
输入: rowIndex = 0
输出: [1]
示例 3:
输入: rowIndex = 1
输出: [1,1]
提示:
0 <= rowIndex <= 33
进阶：
你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
'''


class Solution(object):
    # 时间复杂度O(rowIndex^2)，空间复杂度O(rowIndex^2)
    def getRow(self, rowIndex):
        C = [[0] * (rowIndex + 1) for _ in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            C[i][0] = C[i][i] = 1
            for j in range(i):
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
        return C[rowIndex]

    # 滚动数组空间优化。时间复杂度O(rowIndex^2)，空间复杂度O(rowIndex)
    def getRow2(self, rowIndex):
        row = [0] * (rowIndex + 1)
        for i in range(rowIndex + 1):
            row[0] = 1
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        return row


if __name__ == '__main__':
    u = Solution()
    print(u.getRow(3))  # [1,3,3,1]
    print(u.getRow(0))  # [1]
    print(u.getRow(1))  # [1,1]

    print(u.getRow2(3))  # [1,3,3,1]
    print(u.getRow2(0))  # [1]
    print(u.getRow2(1))  # [1,1]

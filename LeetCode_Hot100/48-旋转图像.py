'''
给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。
说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # 转置
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        # 每行逆序，翻转
        for i in range(n):
            matrix[i].reverse()
        return matrix



if __name__ == '__main__':
    u = Solution()
    m = [[1,2,3],
         [4,5,6],
         [7,8,9]]
    print(u.rotate(m))

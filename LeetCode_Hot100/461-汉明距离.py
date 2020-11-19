'''
两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。
给出两个整数 x 和 y，计算它们之间的汉明距离。
注意：
0 ≤ x, y < 231.
输入: x = 1, y = 4
输出: 2
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y
        dis = 0
        while xor:
            if xor & 1:
                dis += 1
            xor = xor >> 1
        return dis
# 时间复杂度O(1)
# 空间复杂度O(1)

if __name__ == '__main__':
    u = Solution()
    x = 1
    y = 8
    print(u.hammingDistance(x, y))
'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
示例 1：
输入：n = 1    输出：true
解释：2^0 = 1
示例 2：
输入：n = 16   输出：true
解释：2^4 = 16
示例 3：
输入：n = 3    输出：false
示例 4：
输入：n = 4    输出：true
示例 5：
输入：n = 5    输出：false
'''


class Solution:
    # 位运算。时间复杂度(1)，空间复杂度O(1)
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1) == 0)


'''
若 n = 2^x ，则一定满足以下条件：
（1）恒有 n & (n - 1) == 0，这是因为：n 二进制最高位为 1，其余所有位为 0；
    n - 1 二进制最高位为 0，其余所有位为 1；
（2）一定满足 n > 0。
'''

if __name__ == '__main__':
    u = Solution()
    print(u.isPowerOfTwo(1))  # True
    print(u.isPowerOfTwo(16))  # True
    print(u.isPowerOfTwo(3))  # False
    print(u.isPowerOfTwo(4))  # True
    print(u.isPowerOfTwo(5))  # False

'''
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。
该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。
示例 1：
输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
示例 2：
输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2
示例 3：
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
提示：
0 <= n <= 30
'''


class Solution:
    # 时间复杂度O(n)，空间复杂度O(1)
    def fib(self, n):
        if n < 2:
            return n
        f0, f1 = 0, 1
        f2 = f0 + f1
        for i in range(2, n + 1):
            f2 = f0 + f1
            f0 = f1
            f1 = f2
        return f2


if __name__ == '__main__':
    u = Solution()
    print(u.fib(2))  # 1
    print(u.fib(3))  # 2
    print(u.fib(4))  # 3

'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
'''


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        f1, f2, f3 = 1, 2, 3
        for i in range(3, n+1):
            f3 = f1 + f2
            f1 = f2
            f2 = f3
        return f3

if __name__ == '__main__':
    u = Solution()
    n = 10
    print(u.climbStairs(n))
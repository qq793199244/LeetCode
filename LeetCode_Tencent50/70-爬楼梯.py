'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
示例 1：
输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：
输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''


class Solution:
    # 直接动态规划；时间复杂度O(n)；空间复杂度O(n)
    def climbStairs1(self, n):
        dp = [1 for _ in range(n + 1)]
        # 为什么加这句赋值会报错
        # dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    # 用字典；时间复杂度O(n)；空间复杂度O(n)
    def climbStairs(self, n):
        dp = {}
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    # 动态规划优化；时间复杂度O(n)；空间复杂度O(1)
    def climbStairs2(self, n):
        if n == 0: return 1
        if n <= 2: return n
        f0, f1, f2 = 1, 1, 2
        for i in range(3, n + 1):
            f0 = f1
            f1 = f2
            f2 = f0 + f1
        return f2


if __name__ == '__main__':
    u = Solution()
    print(u.climbStairs1(0))
    print(u.climbStairs1(1))
    print(u.climbStairs1(2))
    print(u.climbStairs1(3))
    print(u.climbStairs1(5))
    print(u.climbStairs1(10))
    print('-------------------')
    print(u.climbStairs(0))
    print(u.climbStairs(1))
    print(u.climbStairs(2))
    print(u.climbStairs(3))
    print(u.climbStairs(5))
    print(u.climbStairs(10))
    print('-------------------')
    print(u.climbStairs2(0))
    print(u.climbStairs2(1))
    print(u.climbStairs2(2))
    print(u.climbStairs2(3))
    print(u.climbStairs2(5))
    print(u.climbStairs2(10))

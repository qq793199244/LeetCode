'''
编写一个程序，找出第 n 个丑数。
丑数就是质因数只包含 2, 3, 5 的正整数。
示例:
输入: n = 10      输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:
1 是丑数。
n 不超过1690。
'''


class Solution:
    # 动态规划+3指针；时间复杂度O(n)，空间复杂度O(n)
    def nthUglyNumber(self, n):
        if n == 0:
            return
        dp = [0] * (n+1)
        dp[1] = 1
        p2, p3, p5 = 1, 1, 1
        for i in range(2, n+1):
            dp[i] = min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5)
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1
        return dp[n]


if __name__ == '__main__':
    u = Solution()
    print(u.nthUglyNumber(10))
    print(u.nthUglyNumber(0))
    print(u.nthUglyNumber(1))
    print(u.nthUglyNumber(2))
    print(u.nthUglyNumber(1690))

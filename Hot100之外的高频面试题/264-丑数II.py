'''
编写一个程序，找出第 n 个丑数。
丑数就是质因数只包含 2, 3, 5 的正整数。
示例:输入: n = 10   输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
说明:  1 是丑数。 n 不超过1690。
'''

class Solution(object):
    def nthUglyNumber(self, n):
        dp = [0] * (n+1)
        dp[1] = 1
        i2 = i3 = i5 = 1
        for i in range(2, n+1):
            dp[i] = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            if dp[i] == 2 * dp[i2]:
                i2 += 1
            if dp[i] == 3 * dp[i3]:
                i3 += 1
            if dp[i] == 5 * dp[i5]:
                i5 += 1
        return dp[n]


if __name__ == '__main__':
    u = Solution()
    n = 10
    print(u.nthUglyNumber(n))

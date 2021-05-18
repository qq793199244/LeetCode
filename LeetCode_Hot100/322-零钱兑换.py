'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。
示例 1：
输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：
输入：coins = [2], amount = 3
输出：-1
示例 3：
输入：coins = [1], amount = 0
输出：0
示例 4：
输入：coins = [1], amount = 1
输出：1
示例 5：
输入：coins = [1], amount = 2
输出：2
'''


class Solution:
    '''
    转化为是否可以用 coins 中的数组合和成 amount，完全背包问题，并且为“不考虑排列顺序的完全背包问题”，外层循环为选择池 coins，内层循环为 amount。
    dp[i] 表示和为 i 的 coin 组合中硬币最少有 dp[i] 个。
        外层遍历 coins 每个 coin；
        内层遍历 amount。
    对于元素之和等于 i - coin 的每一种组合，在最后添加 coin 之后即可得到一个元素之和等于 i 的组合，因此在计算 dp[i] 时，应该计算所有的 dp[i − coin] + 1 中的最小值。
    dp[i] = min(dp[i], dp[i - coin] + 1)
    对于边界条件，我们定义 dp[0] = 0。
    最后返回 dp[amount]
    '''

    # 时间复杂度O(amount*n)，n为数组coins的大小，空间复杂度O(amount)
    def coinChange(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[-1] if dp[-1] != float('inf') else -1


if __name__ == '__main__':
    u = Solution()
    print(u.coinChange(coins=[1, 2, 5], amount=11))  # 3
    print(u.coinChange(coins=[2], amount=3))  # -1
    print(u.coinChange(coins=[1], amount=0))  # 0
    print(u.coinChange(coins=[1], amount=1))  # 1
    print(u.coinChange(coins=[1], amount=2))  # 2

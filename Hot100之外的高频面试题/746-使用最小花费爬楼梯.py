'''
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。
每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。
请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
示例 1：
输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
示例 2：
输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
提示：
cost 的长度范围是 [2, 1000]。
cost[i] 将会是一个整型数据，范围为 [0, 999] 。
'''


class Solution(object):
    # 时间复杂度O(n)，空间复杂度O(n)
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]

    # 时间复杂度O(n)，空间复杂度O(1)
    def minCostClimbingStairs2(self, cost):
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, nxt
        return curr


if __name__ == '__main__':
    u = Solution()
    print(u.minCostClimbingStairs([10, 15, 20]))  # 15
    print(u.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6

    print(u.minCostClimbingStairs2([10, 15, 20]))  # 15
    print(u.minCostClimbingStairs2([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))  # 6

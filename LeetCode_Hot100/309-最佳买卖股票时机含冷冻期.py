'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:
输入: [1,2,3,0,2] 输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
'''
class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            # 手上持有股票的最大收益
            p0 = max(f0, f2-prices[i])
            # 手上不持有股票，且处于冷冻期中的累计最大收益
            p1 = f0 + prices[i]
            # 手上不持有股票，且不在冷冻期中的累计最大收益
            p2 = max(f1, f2)
            f0, f1, f2 = p0, p1, p2
        return max(f1, f2)


if __name__ == '__main__':
    u = Solution()
    p1 = [1,2,3,0,2]
    p2 = []
    print(u.maxProfit(p1))
    print(u.maxProfit(p2))
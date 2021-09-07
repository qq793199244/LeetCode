'''
你是一个专业的小偷，计划偷窃沿街的房屋。
每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
示例 1：
输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
   偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：
输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
    偷窃到的最高金额 = 2 + 9 + 1 = 12 。
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 400
'''


class Solution(object):
    # 动态规划。时间复杂度O(n)，空间复杂度O(n)
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        # 如果只有一间
        if n == 1:
            return nums[0]
        dp = [0 for _ in range(n)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            # 如果选中第i间，那么要算出前i-2间中最多，再加第i间的；如果不选第i间，要算前i-1间最多的
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]

    # 动态规划优化。时间复杂度O(n)，空间复杂度O(1)
    def rob2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            # 滚动数组。每间房屋的最高总金额只和该房屋的前两间房屋的最高总金额相关，在每个时刻只需要存储前两间房屋的最高总金额。
            first, second = second, max(first + nums[i], second)
        return second


if __name__ == '__main__':
    u = Solution()
    print(u.rob([1, 2, 3, 1]))  # 4
    print(u.rob([2, 7, 9, 3, 1]))  # 12
    print(u.rob([0]))  # 0

    print(u.rob2([1, 2, 3, 1]))  # 4
    print(u.rob2([2, 7, 9, 3, 1]))  # 12
    print(u.rob2([0]))  # 0

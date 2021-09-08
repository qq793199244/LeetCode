'''
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。
这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
示例 1：
输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
示例 2：
输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。偷窃到的最高金额 = 1 + 3 = 4 。
示例 3：
输入：nums = [0]
输出：0
提示：
1 <= nums.length <= 100
0 <= nums[i] <= 1000
'''


class Solution:
    # 动态规划。时间复杂度O(n)，空间复杂度O(n)
    def rob(self, nums):
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # 不抢最后一个
        dp1 = [0 for _ in range(n)]
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        # 不抢第一个
        dp2 = [0 for _ in range(n)]
        dp2[0] = 0
        dp2[1] = nums[1]
        for i in range(2, n):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[n - 2], dp2[n - 1])

    # 重构成一个方法。
    def rob2(self, nums):
        def robRange(nums, start, end):
            if start == end:
                return nums[start]
            dp = [0 for _ in range(len(nums))]
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            return dp[end]

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        # 不抢第一个
        res1 = robRange(nums, 1, n - 1)
        # 不抢最后一个
        res2 = robRange(nums, 0, n - 2)
        return max(res1, res2)

    # 优化。时间复杂度O(n)，空间复杂度O(1)
    def rob3(self, nums):
        def robRange(nums, start, end):
            if start == end:
                return nums[0]
            first = nums[start]
            second = max(nums[start], nums[start + 1])
            for i in range(start + 2, end + 1):
                first, second = second, max(first + nums[i], second)
            return second

        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        res1 = robRange(nums, 0, n - 2)
        res2 = robRange(nums, 1, n - 1)
        return max(res1, res2)


if __name__ == '__main__':
    u = Solution()
    print(u.rob([2, 3, 2]))  # 3
    print(u.rob([1, 2, 3, 1]))  # 4
    print(u.rob([0]))  # 0
    print(u.rob([0, 0]))  # 0

    print(u.rob2([2, 3, 2]))  # 3
    print(u.rob2([1, 2, 3, 1]))  # 4
    print(u.rob2([0]))  # 0
    print(u.rob2([0, 0]))  # 0

    print(u.rob3([2, 3, 2]))  # 3
    print(u.rob3([1, 2, 3, 1]))  # 4
    print(u.rob3([0]))  # 0
    print(u.rob3([0, 0]))  # 0
    print(u.rob3([1, 2]))  # 2

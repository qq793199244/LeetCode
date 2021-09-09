'''
给你一个整数数组 nums，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i]，删除它并获得 nums[i]的点数。
之后，你必须删除 所有 等于nums[i] - 1 和 nums[i] + 1的元素。
开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。
示例 1：
输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。
示例 2：
输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。
提示：
1 <= nums.length <= 2 * 10^4
1 <= nums[i] <= 10^4
'''


class Solution:
    # 时间复杂度O(n+m)，空间复杂度O(m)，n是数组nums的长度，m是数组中的最大值
    def deleteAndEarn(self, nums):
        if not nums:
            return 0
        # 找出数组中最大的数
        maxVal = max(nums)
        total = [0] * (maxVal + 1)
        # 因此若选择了 x，所有等于 x 的元素也应一同被选择，以尽可能多地获得点数。
        # 用一个数组 记录数组中所有相同元素之和
        for val in nums:
            total[val] += val

        # 打家劫舍
        def rob(nums):
            n = len(nums)
            if n == 1:
                return nums[0]
            first, second = nums[0], max(nums[0], nums[1])
            for i in range(2, n):
                first, second = second, max(first + nums[i], second)
            return second

        return rob(total)


if __name__ == '__main__':
    u = Solution()
    print(u.deleteAndEarn([3, 4, 2]))  # 6
    print(u.deleteAndEarn([2, 2, 3, 3, 3, 4]))  # 9
    print(u.deleteAndEarn([0]))  # 0
    print(u.deleteAndEarn([0, 1]))  # 1
    print(u.deleteAndEarn([]))  # 0

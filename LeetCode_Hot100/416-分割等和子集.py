'''
给你一个只包含正整数的非空数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。
'''


class Solution:
    '''
    本题要求把数组分成两个等和的子集，相当于找到一个子集，其和为 sum / 2，
    这个 sum / 2 就是 target（target 间接给出）。
    于是转化为是否可以用 nums 中的数组合和成 target，01 背包问题，外层循环为选择池 num: nums，内层循环为 target。
    dp[i] 表示是否存在和为 i 的 num 组合。
        外层遍历 nums 每个 num；
        内层遍历 target（由大到小）。
    对于元素之和等于 i - num 的每一种组合，在最后添加 num 之后即可得到一个元素之和等于 i 的组合，因此dp[i] 依赖于 dp[i - num]，并且在计算 dp[i - num] 时，要保证索引较小的元素值不被覆盖，需要后向更新 dp[i]，并且当 i - num < i 时， dp[i] 已经更新过，于是：
    dp[i] = dp[i] || dp[i - num]
    对于特例：如果 sum 为奇数，那一定找不到符合要求的子集，返回 False。
    对于边界条件，我们定义 dp[0] = true 表示当 i - num = 0，存在一个 num 和为 i。
    最后返回 dp[target]。
    【一套框架解决背包问题】https://leetcode-cn.com/problems/target-sum/solution/yi-tao-kuang-jia-jie-jue-bei-bao-wen-ti-58wvk/
    '''

    def canPartition(self, nums):
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    u = Solution()
    print(u.canPartition([1, 5, 11, 5]))  # True
    print(u.canPartition([1, 2, 3, 5]))  # False
    print(u.canPartition([]))  # True

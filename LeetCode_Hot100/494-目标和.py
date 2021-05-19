'''
给你一个整数数组 nums 和一个整数 target 。
向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：
例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。
返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。
示例 1：
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
示例 2：
输入：nums = [1], target = 1
输出：1
'''


class Solution:
    '''
    我们想要的 S = 正数和 + 负数和 = x + y
    而已知 x 与 y 的和是数组总和：x + y = sum
    可以求出 x = (S + sum) / 2 = target
    也就是我们要从 nums 数组里选出几个数，令其和为 target（target 间接给出）。
    于是转化为是否可以用 nums 中的数组合和成 target，01 背包问题，外层循环为选择池 nums，内层循环为 target。
    dp[i] 表示和为 i 的 num 组合有 dp[i] 种。
        外层遍历 nums 每个 num；
        内层遍历 target（由大到小）。
    对于元素之和等于 i - num 的每一种排列，在最后添加 num 之后即可得到一个元素之和等于 i 的排列，因此在计算 dp[i] 时，应该计算所有的 dp[i − num] 之和。
    dp[i] = dp[i] + dp[i - num]
    对于边界条件，我们定义 dp[0] = 1 表示只有当不选取任何元素时，元素之和才为 0，因此只有 1 种方案。
    最后返回 dp[target]
    '''

    def findTargetSumWays(self, nums, target):
        # 设正数和为x，负数和为y；由x+y=tot，x-y=target可以算出x来
        tot = sum(nums)
        # 达不到要求
        if target > tot or (target + tot) % 2:
            return 0
        # 无放回的01背包问题
        x = (tot + target) // 2
        dp = [0] * (x + 1)
        dp[0] = 1
        for num in nums:
            # 倒着防止数字重复使用
            for i in range(x, num - 1, -1):
                dp[i] += dp[i - num]
        return dp[-1]


if __name__ == '__main__':
    u = Solution()
    print(u.findTargetSumWays([1, 1, 1, 1, 1], 3))  # 5
    print(u.findTargetSumWays([1], 1))  # 1

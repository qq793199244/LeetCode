'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
示例 1：
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：
输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：
输入：nums = [1]
输出：[[1]]
提示：
1 <= nums.length <= 6
-10 <= nums[i] <= 10
nums 中的所有整数 互不相同
'''


class Solution:
    # 回溯法。时间复杂度O(n*n!)，空间复杂度O(n)
    def permute(self, nums):
        res = []

        def backtrace(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrace(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrace(nums, [])
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.permute([1, 2, 3]))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    print(u.permute([0, 1]))  # [[0,1],[1,0]]
    print(u.permute([1]))  # [[1]]

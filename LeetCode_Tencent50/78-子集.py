'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
示例 1：
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：
输入：nums = [0]
输出：[[],[0]]
'''


class Solution:
    # 回溯法。时间复杂度O(n*n!)，空间复杂度O(n)
    def subsets(self, nums):
        n = len(nums)
        res = []

        def backtrace(i, tmp):
            res.append(tmp)
            for i in range(i, n):
                backtrace(i + 1, tmp + [nums[i]])

        backtrace(0, [])
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.subsets([1, 2, 3]))  # [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    print(u.subsets([0]))  # [[],[0]]

'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
 [[3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []]
'''
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        if n == 0:
            return []
        res = []

        def dfs(idx, tmp_res):
            res.append(tmp_res)
            for i in range(idx, n):
                dfs(i + 1, tmp_res + [nums[i]])

        dfs(0, [])
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [1,2,3]
    nums2 = []
    print(u.subsets(nums1))
    print(u.subsets(nums2))
'''
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。
示例 1：
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：
输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：
输入：nums = [3,3], target = 6
输出：[0,1]
'''


class Solution:
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def twoSum(self, nums, target):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

    # 哈希表另一种写法。
    def twoSum2(self, nums, target):
        n = len(nums)
        hashtable = {}
        for i in range(n):
            if target - nums[i] in hashtable:
                return [hashtable[target - nums[i]], i]
            else:
                hashtable[nums[i]] = i
        return []


if __name__ == '__main__':
    u = Solution()
    print(u.twoSum([2, 7, 11, 15], 9))  # [0,1]
    print(u.twoSum([3, 2, 4], 6))  # [1,2]
    print(u.twoSum([3, 3], 6))  # [0,1]
    print(u.twoSum([], 1))  # []
    print(u.twoSum([1], 1))

    print(u.twoSum2([2, 7, 11, 15], 9))  # [0,1]
    print(u.twoSum2([3, 2, 4], 6))  # [1,2]
    print(u.twoSum2([3, 3], 6))  # [0,1]
    print(u.twoSum2([], 1))  # []
    print(u.twoSum2([1], 1))

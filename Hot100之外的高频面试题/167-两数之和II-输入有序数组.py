'''
给定一个已按照升序排列的整数数组 numbers ，请你从数组中找出两个数满足相加之和等于目标数 target 。
函数应该以长度为 2 的整数数组的形式返回这两个数的下标值。numbers 的下标 从 1 开始计数 ，
所以答案数组应当满足 1 <= answer[0] < answer[1] <= numbers.length 。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例 1：
输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。
示例 2：
输入：numbers = [2,3,4], target = 6
输出：[1,3]
示例 3：
输入：numbers = [-1,0], target = -1
输出：[1,2]
'''


class Solution:
    # 暴力。时间复杂度O(n^2)，空间复杂度O(1)
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i + 1, j + 1]
        return []

    # 哈希。时间复杂度O(n)，空间复杂度O(n)
    def twoSum2(self, nums, target):
        n = len(nums)
        hash = dict()
        for i in range(n):
            if target - nums[i] in hash:
                # nums是升序数组，所以先写已经出现在哈希表中的
                return [hash[target - nums[i]], i + 1]
            else:
                hash[nums[i]] = i + 1
        return []

    # 双指针碰撞。时间复杂度O(n)，空间复杂度O(1)
    def twoSum3(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            if nums[left] + nums[right] == target:
                return [left + 1, right + 1]
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == '__main__':
    u = Solution()
    print(u.twoSum([2, 7, 11, 15], target=9))  # [1,2]
    print(u.twoSum([2, 3, 4], target=6))  # [1,3]
    print(u.twoSum([-1, 0], target=-1))  # [1,2]

    print(u.twoSum2([2, 7, 11, 15], target=9))  # [1,2]
    print(u.twoSum2([2, 3, 4], target=6))  # [1,3]
    print(u.twoSum2([-1, 0], target=-1))  # [1,2]

    print(u.twoSum3([2, 7, 11, 15], target=9))  # [1,2]
    print(u.twoSum3([2, 3, 4], target=6))  # [1,3]
    print(u.twoSum3([-1, 0], target=-1))  # [1,2]

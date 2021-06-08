'''
给定一个整数数组，判断是否存在重复元素。
如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。
示例 1:
输入: [1,2,3,1]
输出: true
示例 2:
输入: [1,2,3,4]
输出: false
示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''


class Solution:
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def containsDuplicate(self, nums):
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        for i in d:
            if d[i] != 1:
                return True
        return False


if __name__ == '__main__':
    u = Solution()
    print(u.containsDuplicate([1, 2, 3, 1]))  # True
    print(u.containsDuplicate([1, 2, 3, 4]))  # False
    print(u.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True

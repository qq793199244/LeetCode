'''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target，
写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
'''
class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
# 时间复杂度O(logn)
# 空间复杂度O(1)

if __name__ == '__main__':
    u = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(u.search(nums, target))
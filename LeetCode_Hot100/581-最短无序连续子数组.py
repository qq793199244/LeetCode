'''
给你一个整数数组 nums ，你需要找出一个 连续子数组 ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。
请你找出符合题意的 最短 子数组，并输出它的长度。
示例 1：
输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。
示例 2：
输入：nums = [1,2,3,4]
输出：0
示例 3：
输入：nums = [1]
输出：0
'''


class Solution:
    # 排序+双指针。时间复杂度O(nlogn)，空间复杂度O(n)
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        nums1 = sorted(nums)
        left = 0
        right = n - 1
        while left < n and right >= 0:
            if nums[left] == nums1[left]:
                left += 1
            if nums[right] == nums1[right]:
                right -= 1
            if left != n and right != 0:
                if nums[left] != nums1[left] and nums[right] != nums1[right]:
                    break
        return right - left + 1 if right - left > 0 else 0


if __name__ == '__main__':
    u = Solution()
    print(u.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))  # 5
    print(u.findUnsortedSubarray([1, 2, 3, 4]))  # 0
    print(u.findUnsortedSubarray([1]))  # 0

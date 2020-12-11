'''
给你一个整数数组 nums，请你将该数组升序排列。
示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
'''
class Solution:
    def sortArray(self, nums):
        n = len(nums)
        if n == 0:
            return []
        def quickSort(nums, left, right):
            if left >= right:
                return 0
            baseNumber = nums[left]
            i = left
            j = right
            while i != j:
                while j > i and nums[j] >= baseNumber:
                    j -= 1
                if j > i:
                    nums[i], nums[j] = nums[j], nums[i]

                while i < j and nums[i] <= baseNumber:
                    i += 1
                if i < j:
                    nums[i], nums[j] = nums[j], nums[i]
            quickSort(nums, left, i - 1)
            quickSort(nums, i + 1, right)
        quickSort(nums, 0, n-1)
        return nums


if __name__ == '__main__':
    u = Solution()
    nums1 = [5,2,3,1]
    nums2 = [5,1,1,2,0,0]
    print(u.sortArray(nums1))
    print(u.sortArray(nums2))
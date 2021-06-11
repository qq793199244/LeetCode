'''
升序排列的整数数组 nums 在预先未知的某个点上进行了旋转
（例如， [0,1,2,4,5,6,7] 经旋转后可能变为 [4,5,6,7,0,1,2] ）。
请你在数组中搜索 target ，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
示例 1：
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
示例 2：
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
示例 3：
输入：nums = [1], target = 0
输出：-1
提示：
1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
nums 中的每个值都 独一无二
nums 肯定会在某个点上旋转
-10^4 <= target <= 10^4
'''


class Solution:
    # 二分法。时间复杂度O(logn)，空间复杂度O(1)
    def search(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            # 左半段有序
            if nums[mid] >= nums[left]:
                # target在左半段
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                # target在右半段
                else:
                    left = mid + 1
            # 右半段有序
            else:
                # target在右半段
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                # target在左半段
                else:
                    right = mid - 1
        return -1


if __name__ == '__main__':
    u = Solution()
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    nums2 = [1]
    nums3 = [1, 3]
    nums4 = [3, 1]
    print(u.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(u.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(u.search([1], 0))  # -1

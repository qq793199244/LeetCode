'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
示例 1：
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
示例 3：
输入：nums1 = [0,0], nums2 = [0,0]
输出：0.00000
示例 4：
输入：nums1 = [], nums2 = [1]
输出：1.00000
示例 5：
输入：nums1 = [2], nums2 = []
输出：2.00000
【进阶：你能设计一个时间复杂度为 O(log (m+n)) 的算法解决此问题吗？】
'''


class Solution(object):
    # 暴力合并排序数组。时间复杂度O(nlogn+mlogm)，空间复杂度O(m+n)
    def findMedianSortedArrays(self, nums1, nums2):
        if not nums1 and not nums2:
            return
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2.0

    # 二分查找。时间复杂度O(log(m+n))，空间复杂度O()
    # 转化成寻找两个有序数组中的第 k 小的数
    def findMedianSortedArrays2(self, nums1, nums2):
        pass


if __name__ == '__main__':
    u = Solution()
    print(u.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2.00000
    print(u.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.50000
    print(u.findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))  # 0.00000
    print(u.findMedianSortedArrays(nums1=[], nums2=[1]))  # 1.00000
    print(u.findMedianSortedArrays(nums1=[2], nums2=[]))  # 2.00000
    print(u.findMedianSortedArrays([], []))

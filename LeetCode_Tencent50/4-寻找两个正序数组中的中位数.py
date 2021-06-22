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
        if not nums1 and not nums2:
            return
        total = len(nums1) + len(nums2)
        # 如果A数组长度+B数组长度total是奇数，则找total/2+1小的元素
        # 即为中位数
        if total % 2 == 1:
            midIndex = total // 2 + 1
            res = self.getKthElement(nums1, nums2, midIndex)
            return float(res)
        # 否则，找total/2，total/2+1这两个元素
        else:
            midIndex_1 = total // 2
            midIndex_2 = total // 2 + 1
            a = self.getKthElement(nums1, nums2, midIndex_1)
            b = self.getKthElement(nums1, nums2, midIndex_2)
            return (a + b) / 2.0

    def getKthElement(self, nums1, nums2, k):
        len1 = len(nums1)
        len2 = len(nums2)
        index1 = 0
        index2 = 0
        while True:
            # 边界情况，当index1越界时，直接返回nums2的第k小元素
            if index1 == len1:
                return nums2[index2 + k - 1]
            # 边界情况，当index2越界时，直接返回nums1的第k小元素
            if index2 == len2:
                return nums1[index1 + k - 1]
            # 边界情况，k等于1时，返回nums1第一个元素和nums2第一个元素较小者
            if k == 1:
                return min(nums1[index1], nums2[index2])
            new_index1 = min(index1 + k // 2, len1) - 1
            new_index2 = min(index2 + k // 2, len2) - 1
            pivot1 = nums1[new_index1]
            pivot2 = nums2[new_index2]
            # 比较nums1[k/2-1]和nums2[k/2-1]
            # 如果nums1的小，则忽略掉nums1[0] - nums1[k/2-1]这些元素
            # 再更新 k，k 要减去忽略掉的那些元素，index1也要更新，待下轮使用
            if pivot1 <= pivot2:
                k -= (new_index1 - index1 + 1)
                index1 = new_index1 + 1
            # 如果nums2的小，则忽略掉nums2[0] - nums2[k/2-1]这些元素
            # 再更新 k，k 要减去忽略掉的那些元素，index2也要更新，待下轮使用
            else:
                k -= (new_index2 - index2 + 1)
                index2 = new_index2 + 1


if __name__ == '__main__':
    u = Solution()

    print(u.findMedianSortedArrays(nums1=[1, 3], nums2=[2]))  # 2.00000
    print(u.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4]))  # 2.50000
    print(u.findMedianSortedArrays(nums1=[0, 0], nums2=[0, 0]))  # 0.00000
    print(u.findMedianSortedArrays(nums1=[], nums2=[1]))  # 1.00000
    print(u.findMedianSortedArrays(nums1=[2], nums2=[]))  # 2.00000
    print(u.findMedianSortedArrays([], []))

    print(u.findMedianSortedArrays2(nums1=[1, 3], nums2=[2]))  # 2.00000
    print(u.findMedianSortedArrays2(nums1=[1, 2], nums2=[3, 4]))  # 2.50000
    print(u.findMedianSortedArrays2(nums1=[0, 0], nums2=[0, 0]))  # 0.00000
    print(u.findMedianSortedArrays2(nums1=[], nums2=[1]))  # 1.00000
    print(u.findMedianSortedArrays2(nums1=[2], nums2=[]))  # 2.00000
    print(u.findMedianSortedArrays2([], []))
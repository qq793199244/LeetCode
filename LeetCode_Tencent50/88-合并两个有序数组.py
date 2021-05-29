'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
示例 1：
输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：
输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
'''


class Solution:
    def merge(self, nums1, m, nums2, n):
        cur = m + n - 1
        while m > 0 and n > 0:
            if nums2[n - 1] > nums1[m - 1]:
                nums1[cur] = nums2[n - 1]
                n -= 1
            else:
                nums1[cur] = nums1[m - 1]
                m -= 1
            cur -= 1
        nums1[:n] = nums2[:n]
        return nums1


if __name__ == '__main__':
    u = Solution()
    print(u.merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))  # [1,2,2,3,5,6]
    print(u.merge(nums1=[1], m=1, nums2=[], n=0))  # [1]

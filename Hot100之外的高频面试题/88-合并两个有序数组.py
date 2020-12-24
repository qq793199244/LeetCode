'''
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
说明：
初始化nums1 和 nums2 的元素数量分别为m 和 n 。
你可以假设nums1有足够的空间（空间大小大于或等于m + n）来保存 nums2 中的元素。
'''

'''双指针，从后向前'''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        p1 = m - 1
        p2 = n - 1
        p = m + n -1
        while p1 >= 0 and p2 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        # num2剩余
        nums1[:p2+1] = nums2[:p2+1]
        return nums1


if __name__ == '__main__':
    u = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(u.merge(nums1, m, nums2, n))
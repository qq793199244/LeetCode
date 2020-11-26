'''
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
说明：
输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：
如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if m == 0 or n == 0:
            return []
        nums1.sort()
        nums2.sort()
        i, j, pre = 0, 0, None
        res = []
        while i < m and j < n:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(u.intersection(nums1, nums2))
'''
给定两个数组，编写一个函数来计算它们的交集。
示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
说明：
输出结果中的每个元素一定是唯一的。
我们可以不考虑输出结果的顺序。
'''
class Solution(object):
    # 排序+双指针
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
                if nums1[i] != pre:
                    res.append(nums1[i])
                    pre = nums1[i]
                i += 1
                j += 1
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(u.intersection(nums1, nums2))
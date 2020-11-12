'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。
示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
'''
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return
        f = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j]+1)
        return max(f)


if __name__ == '__main__':
    u = Solution()
    nums1 = [10,9,2,5,3,7,101,18]
    nums2 = [3, 2, 1]
    nums3 = []
    print(u.lengthOfLIS(nums1))
    print(u.lengthOfLIS(nums2))
    print(u.lengthOfLIS(nums3))
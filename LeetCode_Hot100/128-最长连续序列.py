'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为 O(n) 的解决方案吗？
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
'''
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        max_len = 0
        d = {}
        for i in nums:
            if i not in d:
                left = d.get(i-1, 0)
                right = d.get(i+1, 0)
                cur_len = left + right + 1
                if cur_len > max_len:
                    max_len = cur_len
                d[i] = cur_len
                d[i-left] = cur_len
                d[i+right] = cur_len
        return max_len


if __name__ == '__main__':
    u = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    print(u.longestConsecutive(nums))
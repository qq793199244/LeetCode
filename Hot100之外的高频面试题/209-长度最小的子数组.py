'''
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，
并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
进阶：
如果你已经完成了 O(n) 时间复杂度的解法, 请尝试 O(n log n) 时间复杂度的解法。
'''
class Solution(object):
    # 滑动窗口
    def minSubArrayLen(self, s, nums):
        n = len(nums)
        if n == 0:
            return 0
        count = n + 1
        sub_sum = 0
        i, j = 0, 0
        while j < n:
            sub_sum += nums[j]
            while sub_sum >= s:
                count = min(count, j-i+1)
                sub_sum -= nums[i]
                i += 1
            j += 1
        if count == n + 1:
            return 0
        else:
            return count
# 时间复杂度O(n)
# 空间复杂度O(1)

if __name__ == '__main__':
    u = Solution()
    s = 7
    nums = [2,3,1,2,4,3]
    print(u.minSubArrayLen(s, nums))
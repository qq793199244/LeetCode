'''
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
进阶：
你能在线性时间复杂度内解决此题吗？
示例:
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if n == 0:
            return []
        if k == 1:
            return nums
        res = []
        win = []
        for i, v in enumerate(nums):
            if i >= k and win[0] <= i - k:
                win.pop(0)
            while win and nums[win[-1]] <= v:
                win.pop()
            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res
'''维护窗口，向右移动时左侧超出窗口的值弹出，因为需要的是窗口内的最大值，
所以只要保证窗口内的值是递减的即可，小于新加入的值全部弹出。最左端即为窗口最大值 '''

if __name__ == '__main__':
    u = Solution()
    nums1 = [1,3,-1,-3,5,3,6,7]
    nums2 = []
    k1 = 3
    k2 = 1
    print(u.maxSlidingWindow(nums1, k1))
    print(u.maxSlidingWindow(nums1, k2))
    print(u.maxSlidingWindow(nums2, k1))
    print(u.maxSlidingWindow(nums2, k2))

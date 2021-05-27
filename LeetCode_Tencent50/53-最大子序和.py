'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
示例:
输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:
如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''


class Solution(object):
    # 属于动态规划
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        tmp = 0
        max_sum = nums[0]
        for i in range(n):
            # 一个负数加上后面的数，肯定比后面的数小，所以当之前和小于0时，丢弃，重新算
            if tmp < 0:
                tmp = 0
            tmp += nums[i]
            max_sum = max(tmp, max_sum)
        return max_sum

    def maxSubArray2(self, nums):
        pass



if __name__ == '__main__':
    u = Solution()
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums2 = []
    nums3 = [-2]
    nums4 = [-2, -1]
    print(u.maxSubArray(nums1))
    print(u.maxSubArray2(nums1))
    print(u.maxSubArray(nums2))
    print(u.maxSubArray2(nums2))
    print(u.maxSubArray(nums3))
    print(u.maxSubArray2(nums3))
    print(u.maxSubArray(nums4))
    print(u.maxSubArray2(nums4))

'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
'''

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cur_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            if cur_sum > 0:
                cur_sum += nums[i]
            else:
                cur_sum = nums[i]
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum

if __name__ == '__main__':
    u = Solution()
    n = [-2,1,-3,4,-1,2,1,-5,4]
    print(u.maxSubArray(n))
'''
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution:
    def maxProduct(self, nums):
        left, right, n = 0, 0, len(nums)
        mul, product = 1, float('-inf')
        while left < n:
            while right < n and nums[right] != 0:  # 移动right指针直至遇到0，这中间用mul累计乘积，product记录最大的乘积
                mul *= nums[right]
                right += 1
                product = max(product, mul)
            while left + 1 < right:  # 移动left指针，这中间用mul累计乘积，product记录最大的乘积
                mul /= nums[left]
                left += 1
                product = max(product, mul)
            while right < n and nums[right] == 0:  # 跳过0
                product = max(product, 0)  # 有可能所有子数组的乘积都小于0，所以0也是候选
                right += 1
            left = right
            mul = 1
        return product



if __name__ == '__main__':
    u = Solution()
    print(u.maxProduct([2,3,-2,4])) # 6
    print(u.maxProduct([-2,0,-1]))  # 0
'''
给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 num 中除 nums[i] 之外其余各元素的乘积。
示例:
输入: [1,2,3,4]
输出: [24,12,8,6]
提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。
说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
进阶：
你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
'''


class Solution(object):
    # 左右乘积列表
    def productExceptSelf(self, nums):
        n = len(nums)
        L, R, res = [0] * n, [0] * n, [0] * n
        L[0] = 1
        for i in range(1, n):
            L[i] = nums[i - 1] * L[i - 1]
        R[n - 1] = 1
        for i in reversed(range(n - 1)):
            R[i] = nums[i + 1] * R[i + 1]
        for i in range(n):
            res[i] = L[i] * R[i]
        return res

    # 空间复杂度O(1)的方法
    def productExceptSelf2(self, nums):
        n = len(nums)
        res = [0] * n
        res[0] = 1
        for i in range(1, n):
            res[i] = nums[i - 1] * res[i - 1]
        R = 1
        for i in reversed(range(n)):
            res[i] = res[i] * R
            R *= nums[i]
        return res


if __name__ == '__main__':
    u = Solution()
    nums = [1, 2, 3, 4]
    print(u.productExceptSelf(nums))
    print(u.productExceptSelf2(nums))

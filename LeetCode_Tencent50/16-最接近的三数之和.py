'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
示例：
输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
'''


class Solution:
    # 排序 + 双指针。时间复杂度O(n^2)，空间复杂度O(1)
    def threeSumClosest(self, nums, target):
        n = len(nums)
        nums = sorted(nums)
        res = float('inf')
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                res = total if abs(total - target) < abs(res - target) else res
                if total == target:
                    return total
                elif total < target:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.threeSumClosest(nums=[-1, 2, 1, -4], target=1))  # 2

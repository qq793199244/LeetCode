'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？
请你找出所有和为 0 且不重复的三元组。注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：
输入：nums = []
输出：[]
示例 3：
输入：nums = [0]
输出：[]
'''


class Solution:
    # 排序 + 循环 + 双指针。 时间复杂度O(n^2)，空间复杂度O(1)
    def threeSum(self, nums):
        n = len(nums)
        # 如果数组中，元素小于3个
        if n < 3:
            return []
        # 排序
        nums = sorted(nums)
        res = []
        # 固定 i
        for i in range(n):
            # 如果从前向后扫描，第一个数就大于0，则不可能与后面更大的数相加为0
            if nums[i] > 0:
                return res
            # 如果固定的i相同，退出本次循环，i继续向后走
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            # 确定本轮双指针初始位置
            left, right = i + 1, n - 1
            while left < right:
                # 如果满足条件，添加到res。然后移动指针。
                if nums[left] + nums[right] + nums[i] == 0:
                    res.append([nums[left], nums[i], nums[right]])
                    # 如果left指向的元素与left的下一个元素重复，继续移动指针。
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 如果right指向的元素与right的下一个元素重复，继续移动指针。
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    # 跳过重复的元素，目前指针状态和添加到res前相同。然后移动指针。
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] + nums[i] < 0:
                    left += 1
                else:
                    right -= 1
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(u.threeSum([]))  # []
    print(u.threeSum([0]))  # []
    print(u.threeSum([0, 0, 0]))  # [[0,0,0]]
    print(u.threeSum([-2, 0, 0, 2, 2]))  # [[-2,0,2]]
    print(u.threeSum([-2, 0, 1, 1, 2]))  # [[-2,0,2],[-2,1,1]]

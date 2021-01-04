'''
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
示例 1：
输入：nums = [10,9,2,5,3,7,101,18]     输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：
输入：nums = [0,1,0,3,2,3]         输出：4
示例 3：
输入：nums = [7,7,7,7,7,7,7]       输出：1
提示：
1 <= nums.length <= 2500
-104 <= nums[i] <= 104
进阶：
你可以设计时间复杂度为 O(n^2) 的解决方案吗？
你能将算法的时间复杂度降低到 O(n log(n)) 吗?
'''


class Solution:
    # 动态规划；时间复杂度O(n^2)，空间复杂度O(n)
    def lengthOfLIS(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # 贪心+二分查找；时间复杂度O(nlogn)，空间复杂度O(n)
    '''
    这个题解不错
    https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/yi-bu-yi-bu-tui-dao-chu-guan-fang-zui-you-jie-fa-x/
    '''
    def lengthOfLIS2(self, nums):
        n = len(nums)
        # 数组 tail[i]表示长度为 i 的最长上升子序列的末尾元素的最小值
        tail = [0] * n
        res = 0
        for num in nums:
            i, j = 0, res
            while i < j:
                mid = (i + j) // 2
                if tail[mid] < num:
                    i = mid + 1
                else:
                    j = mid
            tail[i] = num
            if j == res:
                res += 1
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
    nums2 = [0, 1, 0, 3, 2, 3]
    nums3 = [7, 7, 7, 7, 7, 7, 7]
    nums4 = []
    nums5 = [5, 4, 3, 2, 1]
    nums6 = [1, 2, 3, 4, 5]
    nums7 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    print(u.lengthOfLIS(nums1))
    print(u.lengthOfLIS(nums2))
    print(u.lengthOfLIS(nums3))
    print(u.lengthOfLIS(nums4))
    print(u.lengthOfLIS(nums5))
    print(u.lengthOfLIS(nums6))
    print(u.lengthOfLIS(nums7))
    print('-----------------------')
    print(u.lengthOfLIS2(nums1))
    print(u.lengthOfLIS2(nums2))
    print(u.lengthOfLIS2(nums3))
    print(u.lengthOfLIS2(nums4))
    print(u.lengthOfLIS2(nums5))
    print(u.lengthOfLIS2(nums6))
    print(u.lengthOfLIS2(nums7))

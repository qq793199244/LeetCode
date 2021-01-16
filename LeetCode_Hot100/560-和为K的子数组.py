'''
给定一个整数数组和一个整数k，你需要找到该数组中和为k的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :
数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数k的范围是[-1e7, 1e7]。
'''


class Solution:
    # 暴力解法，超时。时间复杂度O(n^2)，空间复杂度O(1)
    def subarraySum1(self, nums, k):
        res = 0
        n = len(nums)
        for i in range(n):
            cur_sum = 0
            for j in range(i, n):
                cur_sum += nums[j]
                if k == cur_sum:
                    res += 1
        return res

    # 前缀和思想，超时。时间复杂度O(n^2)，空间复杂度O(n)
    '''
    pre_sum[3] = pre_sum[2] + nums[2]
    pre_sum[4] = pre_sum[3] + nums[3]
    pre_sum[5] = pre_sum[4] + nums[4]
    pre_sum[5] = pre_sum[2] + nums[2] + nums[3] + nums[4]
    pre_sum[5] - pre_sum[2] = nums[2] + nums[3] + nums[4]
    '''
    def subarraySum2(self, nums, k):
        n = len(nums)
        res = 0
        pre_sum = [0 for _ in range(n+1)]
        for i in range(n):
            pre_sum[i+1] = nums[i] + pre_sum[i]
        # 统计个数
        for i in range(n):
            for j in range(i, n):
                # 注意偏移，得到nums[i, j]区间内的和
                if pre_sum[j+1] - pre_sum[i] == k:
                    res += 1
        return res

    # 前缀和优化，前缀和+哈希。时间复杂度O(n)，空间复杂度O(n)
    def subarraySum3(self, nums, k):
        if not nums:
            return 0
        n = len(nums)
        d = {}
        d[0] = 1  # 和为0的情况为1次
        res = 0
        cur_sum = 0
        for i in range(n):
            cur_sum += nums[i]
            # 字典存储前缀和的值；当前前缀和减去k，则为之前的前缀和，查看是否在字典中存在
            if cur_sum - k in d:
                res += d[cur_sum - k]
            d[cur_sum] = d.get(cur_sum, 0) + 1
        return res



if __name__ == '__main__':
    u = Solution()
    nums1 = [1, 1, 1]
    k = 3
    print(u.subarraySum1(nums1, k))
    print(u.subarraySum2(nums1, k))
    print(u.subarraySum3(nums1, k))

    nums2 = [1, 2, 6, 4, -1, 5]
    k = 3
    print(u.subarraySum1(nums2, k))
    print(u.subarraySum2(nums2, k))
    print(u.subarraySum3(nums2, k))

    nums3 = [1,2,1,2,1]     # 4
    k = 3
    print(u.subarraySum1(nums3, k))
    print(u.subarraySum2(nums3, k))
    print(u.subarraySum3(nums3, k))

    print(u.subarraySum1([], 2))
    print(u.subarraySum2([], 2))
    print(u.subarraySum3([], 2))

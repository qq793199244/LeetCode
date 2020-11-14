'''
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
示例 1 :
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
'''
'''前缀和+hash'''
class Solution(object):
    def subarraySum(self, nums, k):
        cur_sum = 0
        d = {0:1}
        count = 0
        for num in nums:
            cur_sum += num
            if cur_sum - k in d:
                count += d[cur_sum - k]
            if cur_sum in d:
                d[cur_sum] += 1
            else:
                d[cur_sum] = 1
        return count


if __name__ == '__main__':
    u = Solution()
    nums1 = [1, 1, 1]
    nums2 = []
    k = 2
    res1 = u.subarraySum(nums1, k)
    res2 = u.subarraySum(nums2, k)
    print(res1)
    print(res2)
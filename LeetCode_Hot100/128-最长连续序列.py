'''
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
进阶：你可以设计并实现时间复杂度为O(n) 的解决方案吗？
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
提示：
0 <= nums.length <= 104
-109 <= nums[i] <= 109
'''


class Solution:
    # 排序，暴力法。时间复杂度O(nlogn)，空间复杂度O(n)。因为用到了sort()函数实现机制是Timsort。
    # Timsort详解 https://www.cnblogs.com/clement-jiao/p/9243066.html
    def longestConsecutive1(self, nums):
        nums.sort()
        n = len(nums)
        if n == 0 or n == 1:
            return n
        cur_len = 1
        max_len = 1
        for i in range(1, n):
            if nums[i - 1] + 1 == nums[i]:
                cur_len += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                cur_len = 1
            if cur_len > max_len:
                max_len = cur_len
        return max_len

    # 哈希表，左右边界。时间复杂度O(n)，空间复杂度O(n)
    def longestConsecutive2(self, nums):
        if not nums:
            return 0
        max_len = 0
        # 哈希表的key存的是nums中的数，value是目前的连续长度
        d = {}
        for i in nums:
            # 若i不在哈希表中
            if i not in d:
                # 左邻居的value拿出来，如果没有左邻居则赋值0
                left = d.get(i - 1, 0)
                # 右邻居的value拿出来，如果没有右邻居则赋值0
                right = d.get(i + 1, 0)
                # bridge情况
                cur_len = left + right + 1
                if cur_len > max_len:
                    max_len = cur_len
                # 把当前数的value和边界value，都设置为当前长度
                d[i] = d[i - left] = d[i + right] =  cur_len
        return max_len


if __name__ == '__main__':
    u = Solution()
    nums1 = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    nums3 = [1, 2, 0, 1]
    print(u.longestConsecutive1(nums1))
    print(u.longestConsecutive2(nums1))
    print(u.longestConsecutive1(nums2))
    print(u.longestConsecutive2(nums2))
    print(u.longestConsecutive1(nums3))
    print(u.longestConsecutive2(nums3))

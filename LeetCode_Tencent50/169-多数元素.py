'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊n/2⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：
输入：[3,2,3]
输出：3
示例 2：
输入：[2,2,1,1,1,2,2]
输出：2
进阶：
尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
'''


class Solution:
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def majorityElement(self, nums):
        n = len(nums)
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for k in d:
            if d[k] > n // 2:
                return k
        return

    # 排序法。时间复杂度O(nlogn)，空间复杂度O(logn)。自带sorted排序需要使用logn的栈空间。
    def majorityElement2(self, nums):
        n = len(nums)
        nums = sorted(nums)
        return nums[n // 2]

    # 摩尔投票法。时间复杂度O(n)，空间复杂度O(1)
    def majorityElement3(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate


'''摩尔投票法
假设整个数组的众数记做num，则最初的数组中num的数量大于其余所有数。
当采用count计数的时候有两种情况：
1）假设candidate等于num，则当count从1变为0的过程，此区间内num的数量等于其余数的数量，因此以count=0为分界线，数组右端部分的众数仍然为num
2）假设candidate不等于num，则当count从1变为0的过程， 此区间内num的数量小于等于其余数的数量，因此以count=0为分界线，数组右端部分的众数仍然为num
因此，以count=0可以将整个原始数组分为若干部分，count=0右端部分的数组中的众数永远是num，最终必然会筛选出num
'''

if __name__ == '__main__':
    u = Solution()
    print(u.majorityElement([3, 2, 3]))  # 3
    print(u.majorityElement([2, 2, 1, 1, 1, 2, 2]))  # 2

    print(u.majorityElement2([3, 2, 3]))  # 3
    print(u.majorityElement2([2, 2, 1, 1, 1, 2, 2]))  # 2

    print(u.majorityElement3([3, 2, 3]))  # 3
    print(u.majorityElement3([2, 2, 1, 1, 1, 2, 2]))  # 2

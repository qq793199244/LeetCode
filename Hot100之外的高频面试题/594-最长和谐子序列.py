'''
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
示例 1:
输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.
'''

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        d = {}
        res = 0
        for i in nums:
            d[i] = d.get(i, 0) + 1
        for i in d:
            if i+1 in d:
                res = max(res, d[i]+d[i+1])
        return res
# 时间复杂度O(n)
# 空间复杂度(n)

if __name__ == '__main__':
    u = Solution()
    n1 = [1,3,2,2,5,2,3,7]
    n2 = []
    print(u.findLHS(n1))
    print(u.findLHS(n2))
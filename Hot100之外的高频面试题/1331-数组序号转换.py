'''
给你一个整数数组 arr ，请你将数组中的每个元素替换为它们排序后的序号。
序号代表了一个元素有多大。序号编号的规则如下：
序号从 1 开始编号。
一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
每个数字的序号都应该尽可能地小。
示例 1：
输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。
示例 2：
输入：arr = [100,100,100]
输出：[1,1,1]
解释：所有元素有相同的序号。
示例 3：
输入：arr = [37,12,28,9,100,56,80,5,12]
输出：[5,3,4,2,8,6,7,1,3]
'''


class Solution(object):
    # 去重+排序+哈希。时间复杂度O(nlogn)，空间复杂度O(n)
    def arrayRankTransform(self, arr):
        sorted_nums = sorted(set(arr))
        hashtable = {}
        for i, num in enumerate(sorted_nums):
            hashtable[num] = i + 1
        res = []
        for num in arr:
            res.append(hashtable[num])
        return res
'''
2021.8.25 哔哩哔哩笔试第一题
'''

if __name__ == '__main__':
    u = Solution()
    print(u.arrayRankTransform([40, 10, 20, 30]))  # [4,1,2,3]
    print(u.arrayRankTransform([100, 100, 100]))  # [1,1,1]
    print(u.arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]))  # [5,3,4,2,8,6,7,1,3]

'''
给你一个整数数组 arr 和一个整数 difference，请你找出并返回 arr 中最长等差子序列的长度，该子序列中相邻元素之间的差等于 difference 。
子序列 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 arr 派生出来的序列。
示例 1：
输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
示例 2：
输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。
示例 3：
输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。
'''


class Solution(object):
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        dic = {}
        for a in arr:
            dic[a] = dic.get(a - difference, 0) + 1
        return max(dic.values())

        # 一开始的错误想法，等差数列可以不只隔一个
        # curLen, res = 1, 0
        # n = len(arr)
        # for i in range(1, n):
        #     if arr[i] - arr[i - 1] == difference:
        #         curLen += 1
        #     else:
        #         curLen = 1
        #     res = max(res, curLen)
        # return res


if __name__ == '__main__':
    u = Solution()
    print(u.longestSubsequence(arr=[1, 2, 3, 4], difference=1))  # 4
    print(u.longestSubsequence(arr=[1, 3, 5, 7], difference=1))  # 1
    print(u.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))  # 4

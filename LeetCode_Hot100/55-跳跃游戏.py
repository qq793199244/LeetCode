'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
示例 1:
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
'''

'''动态规划，O(n^2)超时了'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        f = [False] * n
        f[0] = True
        for x in range(n):
            for i in range(x):
                if f[i] and i+nums[i] >= x:
                    f[x] = True
                    break
        return f[n-1]

'''贪心算法'''
class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = 0 # index表示可以到达的最远点索引
        for i in range(len(nums)):
            if i <= index:
                index = max(index, i + nums[i])
                if index >= len(nums) - 1:
                    return True
        return False

if __name__ == '__main__':
    u = Solution2()
    nums1 = [2,3,1,1,4]
    nums2 = [3,2,1,0,4]
    print(u.canJump(nums1))
    print(u.canJump(nums2))
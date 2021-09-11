'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
示例 1:
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：
输入： heights = [2,4]
输出： 4
提示：
1 <= heights.length <=10^5
0 <= heights[i] <= 10^4
'''


class Solution(object):
    # 时间复杂度O(n)，空间复杂度O(n)
    def largestRectangleArea(self, heights):
        n = len(heights)
        res = 0
        # 栈底
        stack = [-1]
        for i in range(n):
            # 当栈不为空 且 当前元素比栈顶元素小或等于
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                # 高 × 宽
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for _ in range(len(stack) - 1):
            res = max(res, heights[stack.pop()] * (n - 1 - stack[-1]))
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(u.largestRectangleArea([2, 4]))  # 4

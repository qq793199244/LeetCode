'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [-1]
        max_res = 0
        for i in range(len(heights)):
            while len(stack) > 1 and heights[i] <= heights[stack[-1]]:
                max_res = max(max_res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        for i in range(len(stack)-1):
            max_res = max(max_res, heights[stack.pop()]*(len(heights)-1-stack[-1]))
        return max_res


if __name__ == '__main__':
    u = Solution()
    h = [2,1,5,6,2,3]
    print(u.largestRectangleArea(h))
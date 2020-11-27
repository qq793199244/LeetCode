'''
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
请你统计并返回 grid 中 负数 的数目。
示例 1：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。
示例 2：
输入：grid = [[3,2],[1,0]]
输出：0
'''
class Solution(object):
    def countNegatives(self, grid):
        m = len(grid)
        n = len(grid[0])
        if m == 0 or n == 0:
            return 0
        count = 0
        for i in range(m):
            if grid[i][0] < 0:
                count += n
                continue
            if grid[i][n-1] >= 0:
                continue
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if left == right:
                    count += n - mid
                    break
                if grid[i][mid] < 0:
                    right = mid
                else:
                    left = mid + 1
        return count


if __name__ == '__main__':
    u = Solution()
    grid1 = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    grid2 = grid = [[3,2],[1,0]]
    grid3 = [[5,1,0],[-5,-5,-5]]
    print(u.countNegatives(grid1))
    print(u.countNegatives(grid2))
    print(u.countNegatives(grid3))
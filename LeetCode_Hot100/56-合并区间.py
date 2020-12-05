'''
给出一个区间的集合，请合并所有重叠的区间。
示例 1:
输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:
输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''
class Solution(object):
    def merge(self, intervals):
        n = len(intervals)
        if n == 0:
            return []
        res = []
        intervals.sort(key=lambda i: i[0])
        for i in intervals:
            if len(res) == 0 or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        return res

if __name__ == '__main__':
    u = Solution()
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals2 = [[1, 4], [4, 5]]
    print(u.merge(intervals1))
    print(u.merge(intervals1))
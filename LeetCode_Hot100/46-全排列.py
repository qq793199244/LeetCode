'''
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
 [[1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]]
'''
class Solution(object):
    def permute(self, nums):
        n = len(nums)
        if n <= 1:
            return [nums]
        visited = [False for _ in range(n)]  # 记录哪些元素已经访问
        res = []
        def dfs(numbers, result, cur, visit):
            if len(cur) == len(numbers):
                result.append(cur[:])  # 这里记得用cur[:]或拷贝
                return
            for i in range(len(numbers)):
                if visit[i]:  # 如果已经访问过某元素，直接跳过进下一个元素
                    continue
                cur.append(numbers[i])
                visit[i] = True  # 将访问过的元素标记
                dfs(numbers, result, cur, visit)
                cur.pop()  # 恢复到之前状态
                visit[i] = False  # 恢复到之前状态
        dfs(nums, res, [], visited)
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [1,2,3]
    nums2 = []
    print(u.permute(nums1))
    print(u.permute(nums2))
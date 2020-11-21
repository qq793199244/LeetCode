'''
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：["((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"]
'''
class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
        res = []
        # left,right:可放置的左右括号数
        def dfs(result, left, right, path):
            if left == 0 and right == 0:
                result.append(path)
                return
            if left > 0:
                dfs(result, left - 1, right, path + '(')
            if left < right:
                dfs(result, left, right - 1, path + ')')
        dfs(res, n, n, '')
        return res


if __name__ == '__main__':
    u = Solution()
    n1 = 3
    n2 = 0
    print(u.generateParenthesis(n1))
    print(u.generateParenthesis(n2))

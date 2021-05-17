'''
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
示例 1：
输入：s = "aa" p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2:
输入：s = "aa" p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3：
输入：s = "ab" p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4：
输入：s = "aab" p = "c*a*b"
输出：true
解释：因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5：
输入：s = "mississippi" p = "mis*is*p*."
输出：false
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp问题难就难在状态转移方程！
        m, n = len(s), len(p)
        # 状态转移矩阵从0开始，但是0对应字符串是空字符串，所以字符串下标都要加一
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    if match(i, j):
                        dp[i][j] = dp[i][j] or dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j] or dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    u = Solution()
    print(u.isMatch(s="aa", p="a"))
    print(u.isMatch(s="aa", p="a*"))
    print(u.isMatch(s="ab", p=".*"))
    print(u.isMatch(s="aab", p="c*a*b"))
    print(u.isMatch(s="mississippi", p="mis*is*p*."))

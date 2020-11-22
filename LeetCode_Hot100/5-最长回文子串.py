'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad" 输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd" 输出: "bb"
'''
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        if n <= 1:
            return s
        # 因为是判断子串，根据子串的性质s[i:j]，因此必然涉及到两层循环，也就需要定义二维数组dp
        # 状态初始化：默认为True，可以省去很多计算
        dp = [[True for _ in range(n)] for _ in range(n)]
        max_len = 0
        start = 0
        # 状态转移方程：表示i到j的子串是否是回文子串
        # dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
        # 遍历状态集：因为需要知道j-1，因此j需要从1开始
        for j in range(1, n):
            # 因为是子串，i一定是要小于j
            for i in range(j):
                if s[i] == s[j]:
                    # 如果收尾字符相等，那么直接取决于去掉该收尾的子串
                    dp[i][j] = dp[i + 1][j - 1]
                else:
                    # 如果不相等，不管子串如何，肯定不是回文
                    dp[i][j] = False
                # 更新最大长度
                if dp[i][j] and max_len < j - i:
                    max_len = j - i
                    start = i
        return s[start:start+max_len+1]


if __name__ == '__main__':
    u = Solution()
    s1 = "babad"
    s2 = "cbbd"
    print(u.longestPalindrome(s1))
    print(u.longestPalindrome(s2))
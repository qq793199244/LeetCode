'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
'''


class Solution:
    # 中心扩散法；时间复杂度O(n^2)，
    # 枚举“中心位置”时间复杂度为O(n)，从“中心位置”扩散得到“回文子串”的时间复杂度为O(n)；
    # 空间复杂度O(1)
    def longestPalindrome1(self, s):
        size = len(s)
        if size < 2:
            return s
        max_len = 1
        res = s[0]
        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)
            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > max_len:
                max_len = len(cur_max_sub)
                res = cur_max_sub
        return res
    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一个字符，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是一个空隙，回文串的长度是偶数
        """
        i = left
        j = right
        while i >= 0 and j < size and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i + 1 : j], j - i - 1

    # 动态规划；时间复杂度O(n^2)，空间复杂度O(n^2)
    def longestPalindrome2(self, s):
        n = len(s)
        if n < 2:
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
        return s[start:start + max_len + 1]

    # 动态规划；时间复杂度O(n^2)，空间复杂度O(n^2)
    # 以下代码虽然看起来短了一些，但是丢失了可读性，
    # 逻辑运算符混用，虽然加上了括号表示优先级，但如果没有前文铺垫，很难读懂是什么意思。
    # 不太推荐大家这么写。
    def longestPalindrome3(self, s):
        n = len(s)
        if n < 2:
            return s
        dp = [[False for _ in range(n)] for _ in range(n)]
        max_len = 1
        start = 0
        for j in range(1, n):
            for i in range(0, j):
                dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]


if __name__ == '__main__':
    u = Solution()
    s1 = ""
    s2 = "babad"
    s3 = "cbbd"
    s4 = "a"

    print(u.longestPalindrome1(s1))
    print(u.longestPalindrome1(s2))
    print(u.longestPalindrome1(s3))
    print(u.longestPalindrome1(s4))

    print(u.longestPalindrome2(s1))
    print(u.longestPalindrome2(s2))
    print(u.longestPalindrome2(s3))
    print(u.longestPalindrome2(s4))

    print(u.longestPalindrome3(s1))
    print(u.longestPalindrome3(s2))
    print(u.longestPalindrome3(s3))
    print(u.longestPalindrome3(s4))

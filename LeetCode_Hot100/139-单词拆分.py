'''
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
    注意你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
'''


class Solution:
    # 完全背包问题。时间复杂度O(n^2)，空间复杂度O(n)
    def wordBreak(self, s, wordDict):
        n = len(s)
        dp = [False] * (n + 1)
        # 初始状态为True
        dp[0] = True
        # 若前i-1个字母已经表示成功，而[i, j)在列表中，则说明前j个字母已经表示成功
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


if __name__ == '__main__':
    u = Solution()
    print(u.wordBreak("leetcode", ["leet", "code"]))
    print(u.wordBreak("applepenapple", ["apple", "pen"]))
    print(u.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

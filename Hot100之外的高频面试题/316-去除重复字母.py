'''
给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同
示例 1：
输入：s = "bcabc"
输出："abc"
示例 2：
输入：s = "cbacdcbc"
输出："acdb"
'''
import collections


class Solution(object):
    # 时间复杂度O(n)，空间复杂度O(n)
    def removeDuplicateLetters(self, s):
        if not s:
            return s
        stack = []
        count = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and count[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            count[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    u = Solution()
    print(u.removeDuplicateLetters("bcabc"))  # abc
    print(u.removeDuplicateLetters("cbacdcbc"))  # acdb

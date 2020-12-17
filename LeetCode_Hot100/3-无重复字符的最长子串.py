'''
给定一个字符串，请你找出其中不含有重复字符的最长子串的长度。
示例1:
输入: s = "abcabcbb"  输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb" 输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew" 输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。
示例 4:
输入: s = ""
输出: 0
提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        '''
            滑动窗口 + 双指针
            时间复杂度O(n^2)，遍历字符串O(n)，字符串中判断not in O(n)
            空间复杂度O(n)
        '''
        n = len(s)
        if n == 0:
            return 0
        win = ''
        res = 0
        left, right = 0, 0
        for i in range(n):
            # 如果当前字符与滑动窗口内字符不重复，加入；右指针+1
            if s[i] not in win:
                win += s[i]
                right += 1
                # 记录当前最大长度
                res = max(res, len(win))
            # 如果当前字符与滑动窗口内字符重复，左指针移动到滑动窗口内重复字符的下一个字符，滑动窗口内字符串为从左指针到新加入的字符
            else:
                left = win.index(s[i]) + 1
                win = win[left:] + s[i]
                # 重复后，重新比较最大长度
                res = max(res, len(win))
        return res

    def lengthOfLongestSubstring2(self, s):
        '''
            哈希表
            时间复杂度O(n)，遍历字符串O(n)，字典中判断in O(1)
            空间复杂度O(n)
        '''
        n = len(s)
        if n == 0:
            return 0
        d = {}
        # 初始值为-1，相当于在字符串的左边界的左侧，还没有开始移动
        end = -1
        res = 0
        for idx, c in enumerate(s):
            if c in d:
                end = max(end, d[c])
            d[c] = idx
            res = max(res, idx - end)
        return res


if __name__ == '__main__':
    u = Solution()
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = ""
    s5 = "a"
    print(u.lengthOfLongestSubstring(s1))
    print(u.lengthOfLongestSubstring(s2))
    print(u.lengthOfLongestSubstring(s3))
    print(u.lengthOfLongestSubstring(s4))
    print(u.lengthOfLongestSubstring(s5))
    print('----------------------------')
    print(u.lengthOfLongestSubstring2(s1))
    print(u.lengthOfLongestSubstring2(s2))
    print(u.lengthOfLongestSubstring2(s3))
    print(u.lengthOfLongestSubstring2(s4))
    print(u.lengthOfLongestSubstring2(s5))

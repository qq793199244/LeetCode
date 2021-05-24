'''
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是p 的字母异位词的子串，返回这些子串的起始索引。
字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
示例 1:
输入: s: "cbaebabacd" p: "abc"
输出: [0, 6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。
示例 2:
输入: s: "abab" p: "ab"
输出: [0, 1, 2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。
'''


class Solution:
    # 滑动窗口+字典。时间复杂度O(n)，空间复杂度O(n)
    def findAnagrams(self, s, p):
        res = []
        from string import ascii_lowercase
        dict_p = {}.fromkeys(ascii_lowercase, 0)
        for i in p:
            dict_p[i] += 1
        win = {}.fromkeys(ascii_lowercase, 0)
        left = right = 0
        while right < len(s):
            win[s[right]] += 1
            if win == dict_p:
                res.append(left)
            if right - left + 1 == len(p):
                win[s[left]] -= 1
                left += 1
            right += 1
        return res



if __name__ == '__main__':
    u = Solution()
    print(u.findAnagrams("cbaebabacd", "abc"))  # [0,6]
    print(u.findAnagrams("abab", "ab"))  # [0, 1, 2]

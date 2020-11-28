'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 滑动窗口
        n = len(s)
        if n == 0:
            return 0
        max_len = 0
        end = -1
        d = {}
        for i, c in enumerate(s):
            if c in d:
                end = max(end, d[c])
            max_len = max(max_len, i-end)
            d[c] = i
        return max_len


if __name__ == '__main__':
    u = Solution()
    # abcabcbb
    l1 = 'abcabcbb'
    l2 = ''
    l3 = 'aaaaaaa'
    print(u.lengthOfLongestSubstring(l1))
    print(u.lengthOfLongestSubstring(l2))
    print(u.lengthOfLongestSubstring(l3))

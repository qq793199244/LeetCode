'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        # 滑动窗口
        n = len(s)
        right = 0
        max_len = 0
        lookup = set()
        for left in range(n):
            while right < n and s[right] not in lookup:
                lookup.add(s[right])
                right += 1
            if len(lookup) > max_len:
                max_len = len(lookup)
            lookup.remove(s[left])
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

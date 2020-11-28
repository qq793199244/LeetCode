'''
给你一个仅由大写英文字母组成的字符串，你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
在执行上述操作后，找到包含重复字母的最长子串的长度。
注意:
字符串长度 和 k 不会超过 104。
示例 1:
输入: s = "ABAB", k = 2
输出: 4
解释:
用两个'A'替换为两个'B',反之亦然。
'''
class Solution(object):
    def characterReplacement(self, s, k):
        n = len(s)
        if k >= n:
            return n
        import collections
        # d存储滑动窗口中所有字母出现的次数
        d = collections.defaultdict(int)
        # max_val来存储字典中出现次数最多的字母的出现次数
        max_val = 0
        res = 0
        left = 0
        for right in range(n):
            d[s[right]] += 1
            max_val = max(max_val, d[s[right]])
            while right-left+1-max_val > k:
                d[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res


if __name__ == '__main__':
    u = Solution()
    s = "ABAB"
    k = 2
    print(u.characterReplacement(s, k))
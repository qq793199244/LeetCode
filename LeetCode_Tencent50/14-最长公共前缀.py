'''
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
示例 1：
输入：strs = ["flower","flow","flight"]
输出："fl"
示例 2：
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
提示：
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] 仅由小写英文字母组成
'''


class Solution:
    # 横向扫描。时间复杂度O(mn)，空间复杂度O(1)。其中 m 是字符串数组中的字符串的平均长度，n 是字符串的数量。
    def longestCommonPrefix(self, strs):
        # 返回两个字符串的公共前缀
        def lcp(s1, s2):
            length, index = min(len(s1), len(s2)), 0
            while index < length and s1[index] == s2[index]:
                index += 1
            return s1[:index]

        if not strs:
            return ""
        res, n = strs[0], len(strs)
        for i in range(1, n):
            res = lcp(res, strs[i])
            if not res:
                return ""
        return res

    # 纵向扫描。时间复杂度O(mn)，空间复杂度的O(1)。m是数组中最短字符串的长度，n是字符串的个数
    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""
        # 先排序，得到最短字符串的长度
        strs = sorted(strs)
        length, n = len(strs[0]), len(strs)
        for i in range(length):
            # 以数组中最短的字符串为基准，对数组中每个字符串第i个字符进行比较
            c = strs[0][i]
            for w in range(1, n):
                # 如果有字符串中第i个字符不相等，或达到了最短长度，则返回目前已匹配的公共前缀
                if strs[w][i] != c or i == len(strs[w]):
                    return strs[0][:i]
        # 数组中只有一个字符串
        return strs[0]


if __name__ == '__main__':
    u = Solution()
    print(u.longestCommonPrefix(["flower", "flow", "flight"]))  # "fl"
    print(u.longestCommonPrefix(["dog", "racecar", "car"]))  # ""
    print(u.longestCommonPrefix(["a"]))  # "a"
    print(u.longestCommonPrefix(["ab", "a"]))  # "a"

    print(u.longestCommonPrefix2(["flower", "flow", "flight"]))  # "fl"
    print(u.longestCommonPrefix2(["dog", "racecar", "car"]))  # ""
    print(u.longestCommonPrefix2(["a"]))  # "a"
    print(u.longestCommonPrefix2(["ab", "a"]))  # "a"

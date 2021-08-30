'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。
示例 1：
输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：
输入: s1 = "abc", s2 = "bad"
输出: false
说明：
0 <= len(s1) <= 100
0 <= len(s2) <= 100
'''


class Solution(object):
    def CheckPermutation(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    u = Solution()
    print(u.CheckPermutation(s1="abc", s2="bca"))  # True
    print(u.CheckPermutation(s1="abc", s2="bad"))  # False
    print(u.CheckPermutation(s1="", s2="a"))  # False

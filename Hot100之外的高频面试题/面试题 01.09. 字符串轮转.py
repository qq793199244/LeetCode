'''
字符串轮转。给定两个字符串s1和s2，请编写代码检查s2是否为s1旋转而成（比如，waterbottle是erbottlewat旋转后的字符串）。
示例1:
 输入：s1 = "waterbottle", s2 = "erbottlewat"
 输出：True
示例2:
 输入：s1 = "aa", s2 = "aba"
 输出：False
提示：
字符串长度在[0, 100000]范围内。
说明:
你能只调用一次检查子串的方法吗？
'''


class Solution(object):
    def isFlipedString(self, s1, s2):
        if not s1 and not s2:
            return True
        m, n = len(s1), len(s2)
        if m != n:
            return False
        newS2 = s2 + s2
        return True if s1 in newS2 else False


if __name__ == '__main__':
    u = Solution()
    print(u.isFlipedString(s1='', s2='s'))  # False
    print(u.isFlipedString(s1="waterbottle", s2="erbottlewat"))  # True
    print(u.isFlipedString(s1="aa", s2="aba"))  # False
    print(u.isFlipedString(s1='', s2=''))  # True

'''
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。
'''
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for i in s:
            d[i] = d.get(i,0)+1
        for i in s:
            if d[i] == 1:
                return i
        return ' '


if __name__ == '__main__':
    u = Solution()
    s1 = "abaccdeff"
    s2 = ''
    print(u.firstUniqChar(s1))
    print(u.firstUniqChar(s2))
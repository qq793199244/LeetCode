'''
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
示例1:
输入:
first = "pale"
second = "ple"
输出: True
示例2:
输入:
first = "pales"
second = "pal"
输出: False
'''
class Solution(object):
    def oneEditAway(self, first, second):
        l1, l2 = len(first), len(second)
        if l1 > l2:
            s1, s2 = first, second
        else:
            s1, s2 = second, first
        k = len(s2)
        for i in range(len(s2)):
            if s1[i] != s2[i]:
                k = i
                break
        return s1[k+1:] == s2[k:] or s1[k+1:] == s2[k+1:]

if __name__ == '__main__':
    u = Solution()
    print(u.oneEditAway("pale", "pal"))
    print(u.oneEditAway("pales", "pal"))
    print(u.oneEditAway("pales", ""))

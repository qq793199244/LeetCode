'''
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。
示例 1:   输入: "()"    输出: true
示例2:    输入: "()[]{}"    输出: true
示例3:    输入: "(]"    输出: false
示例4:    输入: "([)]"  输出: false
示例5:    输入: "{[]}"  输出: true
'''


class Solution(object):
    def isValid(self, s):
        dic = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in s:
            if stack and i in dic:
                if stack[-1] == dic[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack

    def isValid2(self, s):
        n = len(s)
        if n % 2 != 0:
            return False
        tmp_stack = []
        d = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            if i == '(' or i == '[' or i == '{':
                tmp_stack.append(i)
            else:
                if not tmp_stack:
                    return False
                elif d[i] == tmp_stack[-1]:
                    tmp_stack.pop()
                else:
                    return False
        return not tmp_stack


if __name__ == '__main__':
    u = Solution()
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "{[]}"
    s6 = "]]"
    s7 = ""
    print(u.isValid(s1))
    print(u.isValid2(s1))
    print(u.isValid(s2))
    print(u.isValid2(s2))
    print(u.isValid(s3))
    print(u.isValid2(s3))
    print(u.isValid(s4))
    print(u.isValid2(s4))
    print(u.isValid(s5))
    print(u.isValid2(s5))
    print(u.isValid(s6))
    print(u.isValid2(s6))

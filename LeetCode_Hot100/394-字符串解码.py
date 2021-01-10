'''
给定一个经过编码的字符串，返回它解码后的字符串。
编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像3a或2[4]的输入。
示例 1：
输入：s = "3[a]2[bc]"      输出："aaabcbc"
示例 2：
输入：s = "3[a2[c]]"       输出："accaccacc"
示例 3：
输入：s = "2[abc]3[cd]ef"      输出："abcabccdcdcdef"
示例 4：
输入：s = "abc3[cd]xyz"        输出："abccdcdcdxyz"
'''


class Solution:
    # 辅助栈法；时间复杂度O(n)，空间复杂度O(n)，n为字符串s中字符的个数
    def decodeString(self, s):
        tmp_stack = []
        num = 0
        res = ""
        for c in s:
            if '0' <= c <= '9':
                # 数值可能不止一位
                num = num * 10 + int(c)
            elif c == '[':
                # 将[前面的次数和字符串存起来，[]结束num置0
                tmp_stack.append([num, res])
                num, res = 0, ""
            elif c == ']':
                # 取出刚才[之前的次数和字符串
                cur_num, sub_res = tmp_stack.pop()
                # 和[]中的字符串连接起来
                res = sub_res + cur_num * res
            else:
                # 如果是字母字符，直接拼接
                res += c
        return res

    # 递归；时间复杂度O()，空间复杂度O()，n为字符串s中字符的个数
    # 思路与辅助栈法一致，不同点在于将 [ 和 ] 分别作为递归的开启与终止条件
    def decodeString2(self, s):
        def dfs(s, i):
            res, num = "", 0
            # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
            while i < len(s):
                if '0' <= s[i] <= '9':
                    num = num * 10 + int(s[i])
                # 遇到'['开始将后续的字符串递归
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += num * tmp
                    num = 0
                # 遇到']'到达递归边界，结束递归，返回新i和处理好的内层res
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res

        return dfs(s, 0)


if __name__ == '__main__':
    u = Solution()
    s1 = "3[a]2[bc]"
    s2 = "3[a2[c]]"
    s3 = "abcabccdcdcdef"
    s4 = "abc3[cd]xyz"

    print(u.decodeString(s1))  # aaabcbc
    print(u.decodeString(s2))  # accaccacc
    print(u.decodeString(s3))  # abcabccdcdcdef
    print(u.decodeString(s4))  # abccdcdcdxyz
    print('----------------------------------')
    print(u.decodeString2(s1))  # aaabcbc
    print(u.decodeString2(s2))  # accaccacc
    print(u.decodeString2(s3))  # abcabccdcdcdef
    print(u.decodeString2(s4))  # abccdcdcdxyz

'''
字符串压缩。利用字符重复出现的次数，编写一种方法，实现基本的字符串压缩功能。
比如，字符串aabcccccaaa会变为a2b1c5a3。若“压缩”后的字符串没有变短，则返回原先的字符串。
你可以假设字符串中只包含大小写英文字母（a至z）。
示例1:
 输入："aabcccccaaa"
 输出："a2b1c5a3"
示例2:
 输入："abbccd"
 输出："abbccd"
 解释："abbccd"压缩后为"a1b2c2d1"，比原字符串长度更长。
提示：
字符串长度在[0, 50000]范围内。
'''


class Solution:
    # 模拟。时间复杂度O(n)，空间复杂度O(1)，不包括输出所占空间
    def compressString(self, S):
        if S == '':
            return S
        res = ''
        pre, count = S[0], 1
        for c in S[1:]:
            if c == pre:
                count += 1
            else:
                res += (pre + str(count))
                pre, count = c, 1
        res += (pre + str(count))
        if len(res) < len(S):
            return res
        else:
            return S


if __name__ == '__main__':
    u = Solution()
    print(u.compressString("aabcccccaaa"))  # "a2b1c5a3"
    print(u.compressString("abbccd"))  # "abbccd"

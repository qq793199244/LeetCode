'''
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。
示例 1：
输入: s = "leetcode"
输出: false
示例 2：
输入: s = "abc"
输出: true
限制：
0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。
'''


class Solution(object):
    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def isUnique(self, astr):
        if not astr:
            return True
        hashtable = {}
        for c in astr:
            hashtable[c] = hashtable.get(c, 0) + 1
        for i in astr:
            if hashtable[i] > 1:
                return False
        return True

    # 集合去重。
    def isUnique2(self, astr):
        return len(astr) == len(set(astr))

    # 位运算
    def isUnique3(self, astr):
        mark = 0
        for char in astr:
            move_bit = ord(char) - ord('a')
            if (mark & (1 << move_bit)) != 0:
                return False
            else:
                mark |= (1 << move_bit)
        return True


if __name__ == '__main__':
    u = Solution()
    print(u.isUnique(''))  # True
    print(u.isUnique('leetcode'))  # False
    print(u.isUnique('abc'))  # True

    print(u.isUnique2(''))  # True
    print(u.isUnique2('leetcode'))  # False
    print(u.isUnique2('abc'))  # True

    print(u.isUnique3(''))  # True
    print(u.isUnique3('leetcode'))  # False
    print(u.isUnique3('abc'))  # True

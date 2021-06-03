'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。
示例 1：
输入：x = 121
输出：true
示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
示例 4：
输入：x = -101
输出：false
'''


class Solution:
    # 暴力法。时间复杂度O(n)，空间复杂度O(n)
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]

    # 数学法。时间复杂度O(logn)，空间复杂度O(1)
    def isPalindrome2(self, x):
        # 负数；个位是0
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        reversedNum = 0
        # 当反转一半时，已反转的位数小于等于x字符串值的一半
        while x > reversedNum:
            reversedNum = reversedNum * 10 + x % 10
            x //= 10
        return x == reversedNum or x == reversedNum // 10


if __name__ == '__main__':
    u = Solution()
    print(u.isPalindrome(121))  # True
    print(u.isPalindrome(-121))  # False
    print(u.isPalindrome(10))  # False
    print(u.isPalindrome(-101))  # False

    print(u.isPalindrome2(121))  # True
    print(u.isPalindrome2(-121))  # False
    print(u.isPalindrome2(10))  # False
    print(u.isPalindrome2(-101))  # False

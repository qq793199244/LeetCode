'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
'''


class Solution:
    # 双指针。时间复杂度O(n)，空间复杂度O(1)
    def reverseString(self, s):
        n = len(s)
        if n <= 1:
            return s
        left, right = 0, n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    u = Solution()
    print(u.reverseString(["h", "e", "l", "l", "o"]))  # ["o","l","l","e","h"]
    print(u.reverseString(["H", "a", "n", "n", "a", "h"]))  # ["h","a","n","n","a","H"]

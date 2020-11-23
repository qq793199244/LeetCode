'''
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
'''
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        if n <= 1:
            return s
        left = 0
        right = n - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s


if __name__ == '__main__':
    u = Solution()
    s1 = ["h","e","l","l","o"]
    s2 = ["H","a","n","n","a","h"]
    s3 = []
    print(u.reverseString(s1))
    print(u.reverseString(s2))
    print(u.reverseString(s3))
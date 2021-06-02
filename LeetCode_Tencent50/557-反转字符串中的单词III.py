'''
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
示例：
输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"
提示：
在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
'''


class Solution:
    # 将字符串分割成单词列表，然后把每个单词反转切片。时间复杂度O(n)，空间复杂度O(n)
    def reverseWords1(self, s):
        return " ".join(word[::-1] for word in s.split(" "))

    # 用两次切片，先反转单词列表，再反转字符串。时间复杂度O(n)，空间复杂度O(n)
    def reverseWords2(self, s):
        return " ".join(s.split(" ")[::-1])[::-1]

    # 先反转字符串，再反转单词列表。时间复杂度O(n)，空间复杂度O(n)
    def reverseWords3(self, s):
        return " ".join(s[::-1].split(" ")[::-1])


if __name__ == '__main__':
    u = Solution()
    print("Let's take LeetCode contest")
    print(u.reverseWords1("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
    print(u.reverseWords2("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"
    print(u.reverseWords3("Let's take LeetCode contest"))  # "s'teL ekat edoCteeL tsetnoc"

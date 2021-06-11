'''
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
示例 1:
输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:
输入: num1 = "123", num2 = "456"
输出: "56088"
说明：
num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
(return str(int(num1) * int(num2)))
'''


class Solution:
    # 时间复杂度O(mn)，空间复杂度O(m+n)
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        m, n = len(num1), len(num2)
        # 让num2是位数少的那个
        if m < n:
            num1, num2 = num2, num1
            m, n = n, m
        res = [0] * (m + n)
        # num2是被乘数
        for i in range(n - 1, -1, -1):
            x = int(num2[i])
            for j in range(m - 1, -1, -1):
                res[i + j + 1] += x * int(num1[j])
        for i in range(m + n - 1, 0, -1):
            res[i - 1] += res[i] // 10
            res[i] %= 10
        index = 1 if res[0] == 0 else 0
        ans = "".join(str(x) for x in res[index:])
        return ans


if __name__ == '__main__':
    u = Solution()
    print(u.multiply(num1="2", num2="3"))  # "6"
    print(u.multiply(num1="123", num2="456"))  # "56088"
    print(u.multiply(num1="9", num2="99"))  # "891"
    print(u.multiply(num1="99", num2="9"))  # "891"

'''
编写一个程序判断给定的数是否为丑数。
丑数就是只包含质因数2, 3, 5的正整数。
示例 1:
输入: 6       输出: true
解释: 6 = 2 × 3
示例 2:
输入: 8       输出: true
解释: 8 = 2 × 2 × 2
示例3
输入: 14      输出: false
解释: 14 不是丑数，因为它包含了另外一个质因数7。
说明：
1是丑数。
输入不会超过 32 位有符号整数的范围:[−231, 231− 1]。
'''
class Solution:
    def isUgly(self, num):
        if num == 0:
            return False
        while True:
            if num == 1:
                return True
            if num % 2 == 0:
                num /= 2
            elif num % 3 == 0:
                num /= 3
            elif num % 5 == 0:
                num /= 5
            else:
                return False

if __name__ == '__main__':
    u = Solution()
    print(u.isUgly(1))
    print(u.isUgly(6))
    print(u.isUgly(8))
    print(u.isUgly(14))
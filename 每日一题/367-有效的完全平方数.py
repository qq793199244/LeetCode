'''
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。
进阶：不要 使用任何内置的库函数，如 sqrt 。
示例 1：
输入：num = 16
输出：true
示例 2：
输入：num = 14
输出：false
提示：
1 <= num <= 2^31 - 1
'''


class Solution:
    # 二分法。时间复杂度O(logn)，空间复杂度O(1)
    def isPerfectSquare(self, num):
        left, right = 0, num
        while left <= right:
            mid = (left + right) // 2
            square = mid ** 2
            if square < num:
                left = mid + 1
            elif square > num:
                right = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    u = Solution()
    print(u.isPerfectSquare(16))  # True
    print(u.isPerfectSquare(14))  # False

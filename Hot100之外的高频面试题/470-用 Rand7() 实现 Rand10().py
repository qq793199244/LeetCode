'''
已有方法rand7可生成 1 到 7 范围内的均匀随机整数，试写一个方法rand10生成 1 到 10 范围内的均匀随机整数。
不要使用系统的Math.random()方法。
示例 1:
输入: 1       输出: [7]
示例 2:
输入: 2       输出: [8,4]
示例 3:
输入: 3       输出: [8,1,10]
提示:
rand7已定义。
传入参数:n表示rand10的调用次数。
进阶:
rand7()调用次数的期望值是多少?
你能否尽量少调用 rand7() ?
'''
from random import randint


class Solution:
    def rand7(self):
        return randint(1, 7)

    # 已知 rand_N() 可以等概率的生成[1, N]范围的随机数
    # 那么：
    # (rand_X() - 1) × Y + rand_Y() ==> 可以等概率的生成[1, X * Y]范围的随机数
    # 即实现了 rand_XY()
    def rand10(self):
        num = (self.rand7() - 1) * 7 + self.rand7()
        while num > 40:
            num = (self.rand7() - 1) * 7 + self.rand7()
        return num % 10 + 1

if __name__ == '__main__':
    u = Solution()
    print(u.rand10())

    '''
    执行用时：356 ms, 在所有 Python 提交中击败了84.52%的用户
    内存消耗：17.9 MB, 在所有 Python 提交中击败了51.19%的用户
    '''

'''
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，
计算其二进制数中的 1 的数目并将它们作为数组返回。
示例 1:
输入: 2   输出: [0,1,1]
示例 2:
输入: 5   输出: [0,1,1,2,1,2]
进阶:
给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。
'''
class Solution1(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num + 1):
            count = 0
            while i:
                count += 1
                i = i & (i - 1)
            res.append(count)
        return res
# 时间复杂度O(n*sizeof(int)),对每一个i都计算一次1的个数
# 空间复杂度O(n)

class Solution2(object):
    '''奇数的二进制中一的位数等于前面的偶数的二进制中1的个数加1,也就是前面偶数的最后一位的0变成1
    偶数的二进制中一的位数等于自身除以2的数的二进制中1的个数,
    偶数除以2相当于右移一位,也就是将最后面的0移出去,不影响1的个数
'''
    def countBits(self, num):
        res = [0] * (num + 1)
        for i in range(1, num + 1):
            if 1 & i:
                res[i] = res[i - 1] + 1
            else:
                res[i] = res[i // 2]
        return res
# 时间复杂度O(n)
# 空间复杂度O(n)

if __name__ == '__main__':
    u = Solution1()
    v = Solution2()
    num1 = 2
    num2 = 5
    print(u.countBits(num1))
    print(u.countBits(num2))
    print(v.countBits(num1))
    print(v.countBits(num2))
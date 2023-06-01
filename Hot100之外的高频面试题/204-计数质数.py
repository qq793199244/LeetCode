'''
给定整数 n ，返回 所有小于非负整数 n 的质数的数量 。
示例 1：
输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：
输入：n = 0
输出：0
示例 3：
输入：n = 1
输出：0
'''


class Solution(object):
    # leetcode超时
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def isPrimes(c):
            if c < 2:
                return False
            for i in range(2, int(c ** 0.5) + 1):
                if c % i == 0:
                    return False
            return True

        res = 0
        for num in range(2, n):
            if isPrimes(num):
                res += 1
        return res

    def countPrimes2(self, n):
        if n < 2:
            return 0
        num_list = [1 for _ in range(n)]
        for i in range(2, int(n ** 0.5) + 1):
            if num_list[i]:
                for j in range(i * i, n, i):
                    num_list[j] = 0
        # res = 0
        # for m in range(2, n):
        #     if num_list[m]:
        #         res += 1
        # return res
        num_list[0] = num_list[1] = 0
        return sum(num_list)


if __name__ == '__main__':
    u = Solution()
    print(u.countPrimes(10))
    print(u.countPrimes(0))
    print(u.countPrimes(1))
    print(u.countPrimes(3))
    print(u.countPrimes(4))
    print(u.countPrimes(2))

    print(u.countPrimes2(10))
    print(u.countPrimes2(0))
    print(u.countPrimes2(1))
    print(u.countPrimes2(3))
    print(u.countPrimes2(4))
    print(u.countPrimes2(2))

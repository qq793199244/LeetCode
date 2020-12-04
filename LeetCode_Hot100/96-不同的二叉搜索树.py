'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
示例:
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''
class Solution(object):
    # 动态规划。时间复杂度O(n^2) 空间复杂度O(n)
    def numTrees1(self, n):
        f = [0] * (n+1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n+1):
            for j in range(1, i+1):
                f[i] += f[j-1] * f[i-j]
        return f[-1]

    # 数学，卡特兰数。时间复杂度O(n) 空间复杂度O(1)
    def numTrees2(self, n):
        c = 1
        for i in range(n):
            c = c * 2 * (2 * i + 1) // (i + 2)
        return c

if __name__ == '__main__':
    u = Solution()
    n1 = 1
    n2 = 10
    print(u.numTrees1(n1))
    print(u.numTrees2(n1))
    print(u.numTrees1(n2))
    print(u.numTrees2(n2))
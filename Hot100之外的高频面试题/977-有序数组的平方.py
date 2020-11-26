'''
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]
'''
class Solution(object):
    # 双指针
    def sortedSquares(self, A):
        n = len(A)
        if n == 0:
            return []
        res = [0] * n
        i, j, pos = 0, n-1, n-1
        while i <= j:
            if A[i] * A[i] > A[j] * A[j]:
                res[pos] = A[i] * A[i]
                i += 1
            else:
                res[pos] = A[j] * A[j]
                j -= 1
            pos -= 1
        return res


if __name__ == '__main__':
    u = Solution()
    A1 = [-4,-1,0,3,10]
    A2 = [-7,-3,2,3,11]
    print(u.sortedSquares(A1))
    print(u.sortedSquares(A2))

'''
给定一个非负整数数组A， A 中一半整数是奇数，一半整数是偶数。
对数组进行排序，以便当A[i] 为奇数时，i也是奇数；当A[i]为偶数时， i 也是偶数。
你可以返回任何满足上述条件的数组作为答案。
示例：
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
提示：
2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000
'''


class Solution:
    def sortArrayByParityII(self, A):
        # 开辟了新空间
        # 时间复杂度O(n)
        # 空间复杂度O(n)
        n = len(A)
        i, j = 0, 1
        res = [0] * n
        for a in A:
            if a % 2 == 0:
                res[i] = a
                i += 2
            else:
                res[j] = a
                j += 2
        return res

    def sortArrayByParityII2(self, A):
        # 不开辟新空间，双指针原地排序。遍历偶数位，如果偶数位不是偶数，就从奇数位找偶数，交换
        # 时间复杂度O(n)
        # 空间复杂度O(1)
        n = len(A)
        i, j = 0, 1
        while i < n:
            if A[i] % 2 == 1:
                while A[j] % 2 == 1:
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 2
        return A


if __name__ == '__main__':
    u = Solution()
    nums = [4, 2, 5, 7]
    print(u.sortArrayByParityII(nums))
    print(u.sortArrayByParityII2(nums))

'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
示例 1:
输入: [2,2,1]
输出: 1
示例 2:
输入: [4,1,2,1,2]
输出: 4
'''


class Solution:
    # 哈希表法。时间复杂度O(n)，空间复杂度O(n)
    def singleNumber(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for i in dic:
            if dic[i] == 1:
                return i

    # 位运算，异或。时间复杂度O(n)，空间复杂度O(1)
    '''
    异或运算有以下三个性质。
    1. 任何数和 0 做异或运算，结果仍然是原来的数
    2. 任何数和其自身做异或运算，结果是 0
    3. 异或运算满足交换律和结合律
    '''
    def singleNumber2(self, nums):
        res = 0
        for i in nums:
            res ^= i
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.singleNumber([2, 2, 1]))  # 1
    print(u.singleNumber([4, 1, 2, 1, 2]))  # 4

    print(u.singleNumber2([2, 2, 1]))  # 1
    print(u.singleNumber2([4, 1, 2, 1, 2]))  # 4
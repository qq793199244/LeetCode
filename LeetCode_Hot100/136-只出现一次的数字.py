'''
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
说明：
你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 根据异或的交换律和结合律
        # a ^ b ^ a = a ^ a ^ b = b
        res = 0
        for i in nums:
            res = res ^ i
        return res

if __name__ == '__main__':
    u = Solution()
    nums = [1, 1, 2, 2, 3, 4, 4]
    print(u.singleNumber(nums))
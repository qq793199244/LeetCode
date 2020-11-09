'''

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d:
                return [d[target-nums[i]], i]
            else:
                d[nums[i]] = i
        return []


if __name__ == '__main__':
    u = Solution()
    # nums = [2, 7, 11, 15], target = 9
    l1 = [2, 7, 11, 15]
    target1 = 9

    l2 = [2, 3, 4, 5, 6]
    target2 = 100

    res1 = u.twoSum(l1, target1)
    res2 = u.twoSum(l2, target2)
    print(res1)
    print(res2)
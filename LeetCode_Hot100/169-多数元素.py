'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return
        hashDict = {}
        for i in nums:
            hashDict[i] = hashDict.get(i, 0) + 1
        for key in hashDict.keys():
            if hashDict[key] > n/2:
                return key

if __name__ == '__main__':
    u = Solution()
    nums1 = []
    nums2 = [1]
    nums3 = [1, 2, 2]
    print(u.majorityElement(nums1))
    print(u.majorityElement(nums2))
    print(u.majorityElement(nums3))
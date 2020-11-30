'''
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
'''
class Solution(object):
    # 哈希表法
    def majorityElement1(self, nums):
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

    # 分治法
    def majorityElement2(self, nums):
        n = len(nums)
        if n == 0:
            return
        def help(low, high):
            left_count = 0
            right_count = 0
            if low == high:
                return nums[low]
            mid = (high - low) // 2 + low
            left = help(low, mid)
            right = help(mid+1, high)
            if left == right:
                return left
            for i in range(low, high+1):
                if nums[i] == left:
                    left_count += 1
            for i in range(low, high+1):
                if nums[i] == right:
                    right_count += 1
            return left if left_count > right_count else right
        return help(0, n-1)



if __name__ == '__main__':
    u = Solution()
    nums1 = []
    nums2 = [1, 2, 2]
    nums3 = [1, 2, 2, 2, 1, 1, 1]
    print(u.majorityElement1(nums1))
    print(u.majorityElement1(nums2))
    print(u.majorityElement1(nums3))
    print(u.majorityElement2(nums1))
    print(u.majorityElement2(nums2))
    print(u.majorityElement2(nums3))
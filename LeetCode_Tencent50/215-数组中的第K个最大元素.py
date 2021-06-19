'''
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:
你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
'''


class Solution(object):
    # 堆排序。时间复杂度O(nlogn)，空间复杂度O(logn)
    def findKthLargest(self, nums, k):
        def adjust_heap(nums, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                adjust_heap(nums, n, largest)

        n = len(nums)
        # 建堆
        for i in range(n, -1, -1):
            adjust_heap(nums, n, i)

        # 一个个交换元素
        for i in range(n - 1, n - k, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjust_heap(nums, i, 0)

        return nums[0]


if __name__ == '__main__':
    u = Solution()
    print(u.findKthLargest([3, 2, 1, 5, 6, 4], k=2))  # 5
    print(u.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))  # 4

'''
在未排序的数组中找到第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
'''


class Solution(object):
    def findKthLargest(self, nums, k):
        """堆排序"""

        def heapify(a, start, end):
            """ 自上向下堆化
                a (list): 输入数组
                start (int): 堆化目标在数组的位置
                end (int): 堆在数组的截止位置
            """
            while True:
                max_pos = start
                if start * 2 + 1 <= end and a[start] < a[start * 2 + 1]:
                    max_pos = start * 2 + 1
                if start * 2 + 2 <= end and a[max_pos] < a[start * 2 + 2]:
                    # 若右叶子节点存在，且大于目标值，则将最大值所在位置指向该节点位置
                    max_pos = start * 2 + 2
                if max_pos == start:
                    break
                # 交换位置
                a[start], a[max_pos] = a[max_pos], a[start]
                start = max_pos

        # 建堆
        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, i, len(nums) - 1)
        # 排序
        i = len(nums) - 1
        while i > len(nums) - 1 - k:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            heapify(nums, 0, i)
        return nums[len(nums) - k]

    def findKthLargest2(self, nums, k):
        def adjustMaxHeap(array, i, n):  # 维护堆，时间复杂度O(logn)
            largest = i  # 假设当前父节点最大
            left = 2 * i + 1
            right = 2 * i + 2
            # 找这三个节点中最大的
            if left < n and array[largest] < array[left]:
                largest = left
            if right < n and array[largest] < array[right]:
                largest = right
            if largest != i:
                array[largest], array[i] = array[i], array[largest]
                adjustMaxHeap(array, largest, n)

        # 建大顶堆,只需要对非叶子结点
        n = len(nums)
        for i in range((n - 1) // 2, -1, -1):
            adjustMaxHeap(nums, i, n)
        # 排序，只需要循环K次，排序TOP K个节点 时间复杂度O(k)
        for i in range(n - 1, n - k - 1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjustMaxHeap(nums, 0, i)
        return nums[n - k]
    # 时间复杂度O(klogn)
    # 空间复杂度O(logn)，递归使用栈空间


if __name__ == '__main__':
    u = Solution()
    # [3,2,1,5,6,4] 和 k = 2
    n = [3, 2, 1, 5, 6, 4]
    k = 2
    # res1 = u.findKthLargest(n, k)
    # print(res1)
    res2 = u.findKthLargest2(n, k)
    print(res2)

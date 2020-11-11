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
                if start*2 + 1 <= end and a[start] < a[start*2+1]:
                    max_pos = start*2 + 1
                if start*2 + 2 <= end and a[max_pos] < a[start*2+2]:
                    # 若右叶子节点存在，且大于目标值，则将最大值所在位置指向该节点位置
                    max_pos = start*2 + 2
                if max_pos == start:
                    break
                # 交换位置
                a[start], a[max_pos] = a[max_pos], a[start]
                start = max_pos

        # 建堆
        for i in range(len(nums)//2-1, -1, -1):
            heapify(nums, i, len(nums)-1)
        # 排序
        i = len(nums) - 1
        while i > len(nums)-1-k:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            heapify(nums, 0, i)
        return nums[len(nums)-k]

if __name__ == '__main__':
    u = Solution()
    # [3,2,1,5,6,4] 和 k = 2
    n = [3,2,1,5,6,4]
    k = 2
    res = u.findKthLargest(n, k)
    print(res)
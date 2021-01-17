'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]       输出: 5
限制：0 <= 数组长度 <= 50000
'''


class Solution:
    # 暴力法，平台超时。时间复杂度O(n^2)，空间复杂度O(1)
    def reverseParis1(self, nums):
        res = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    res += 1
                    res %= 1000000007
        return res

    # 归并排序思想。时间复杂度O(nlogn)，空间复杂度O(n)
    def reverseParis2(self, nums):
        self.count = 0

        # 归并排序
        def merge_sort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            # 拆分
            mid = n // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        # 合并
        def merge(left, right):
            l, r = 0, 0
            tmp = []
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    tmp.append(left[l])
                    l += 1
                else:
                    # 若左边数组第l个元素大于右边第r个元素，则左边数组将有(n-l)个大于右边第r个元素
                    self.count += (len(left) - l)
                    tmp.append(right[r])
                    r += 1
            tmp += left[l:]
            tmp += right[r:]
            return tmp

        merge_sort(nums)
        return self.count


if __name__ == '__main__':
    u = Solution()
    nums1 = []
    nums2 = [1, 2, 3, 4]
    nums3 = [7, 5, 6, 4]
    nums4 = [1, 2, 3, 4, 5, 6, 7, 0]

    print(u.reverseParis1(nums1))
    print(u.reverseParis1(nums2))
    print(u.reverseParis1(nums3))
    print(u.reverseParis1(nums4))
    print('--------------------')
    print(u.reverseParis2(nums1))
    print(u.reverseParis2(nums2))
    print(u.reverseParis2(nums3))
    print(u.reverseParis2(nums4))

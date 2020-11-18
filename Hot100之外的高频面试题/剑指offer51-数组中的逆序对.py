'''
在数组中的两个数字，如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
示例 1:
输入: [7,5,6,4]
输出: 5
'''
class Solution:
    def merge(self, a1, a2):
        l = r = 0
        n1, n2 = len(a1), len(a2)
        res = []
        while l < n1 and r < n2:
            if a1[l] > a2[r]:
                # 若左边数组第l个元素大于右边第r个元素，则左边数组将有(n1-l)个大于右边第r个元素
                self.count += (n1 - l)
                res.append(a2[r])
                r += 1
            else:
                res.append(a1[l])
                l += 1
        return res + a1[l:] + a2[r:]

    def merge_sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        left = self.merge_sort(arr[:n//2])
        right = self.merge_sort(arr[n//2:])
        return self.merge(left, right)

    def reversePairs(self, nums):
        self.count = 0
        self.merge_sort(nums)
        return self.count


if __name__ == '__main__':
    u = Solution()
    nums1 = [7, 5, 6, 4]
    nums2 = []
    print(u.reversePairs(nums1))
    print(u.reversePairs(nums2))
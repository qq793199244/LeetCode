'''
给你两个 没有重复元素 的数组 nums1 和 nums2 ，其中 nums1 是 nums2 的子集。
请你找出 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。
示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于 num1 中的数字 4 ，你无法在第二个数组中找到下一个更大的数字，因此输出 -1 。
    对于 num1 中的数字 1 ，第二个数组中数字1右边的下一个较大数字是 3 。
    对于 num1 中的数字 2 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。
提示：
    1 <= nums1.length <= nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 10^4
    nums1和nums2中所有整数 互不相同
    nums1 中的所有整数同样出现在 nums2 中
    进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗
'''


class Solution:
    # 暴力法。时间复杂度O(m*n)，空间复杂度O(m)
    def nextGreaterElement(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        res = []
        # 遍历 nums1
        for i in range(m):
            # 获取当前元素在 nums2 中的下标
            idx = nums2.index(nums1[i])
            # 如果当前元素在 nums2 中已经是最后一个元素，直接添加-1
            if idx == n - 1:
                res.append(-1)
            # 从 nums2 中当前元素的下一个位置开始判断
            for j in range(idx + 1, n):
                # 如果找到比当前元素大的，添加找到的元素，结束本层循环
                if nums2[j] > nums1[i]:
                    res.append(nums2[j])
                    break
                # 如果遍历完还是没有找到，添加-1
                if j == n - 1:
                    res.append(-1)
        return res

    # 单调栈。时间复杂度O(m+n)，空间复杂度O(n)
    def nextGreaterElement2(self, nums1, nums2):
        res = []
        stack = []
        # 哈希表中默认 nums2 中每个元素赋值为 -1
        hashmap = {num: -1 for num in nums2}
        # 遍历 nums2
        for i in nums2:
            # 当栈不为空，且 当前元素大于栈顶元素
            while stack and i > stack[-1]:
                # 比较小的栈顶元素出栈
                smaller = stack.pop()
                # 在哈希表中存储出栈元素key，value赋值为当前元素
                hashmap[smaller] = i
            # 当前元素进栈
            stack.append(i)
        # 遍历 nums1
        for j in nums1:
            # 结果中添加 nums1 中当前元素在哈希表中的值
            res.append(hashmap[j])
        return res


if __name__ == '__main__':
    u = Solution()
    print(u.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))  # [-1,3,-1]
    print(u.nextGreaterElement(nums1=[2, 4], nums2=[1, 2, 3, 4]))  # [3,-1]
    print(u.nextGreaterElement(nums1=[1, 2], nums2=[1, 2, 3]))  # [2,3]
    print(u.nextGreaterElement(nums1=[4, 1, 2, 5], nums2=[1, 3, 4, 2, 5]))  # [5,3,5,-1]

    print(u.nextGreaterElement2(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))  # [-1,3,-1]
    print(u.nextGreaterElement2(nums1=[2, 4], nums2=[1, 2, 3, 4]))  # [3,-1]
    print(u.nextGreaterElement2(nums1=[1, 2], nums2=[1, 2, 3]))  # [2,3]
    print(u.nextGreaterElement2(nums1=[4, 1, 2, 5], nums2=[1, 3, 4, 2, 5]))  # [5,3,5,-1]

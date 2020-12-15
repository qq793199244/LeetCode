'''
给定一个非空的整数数组，返回其中出现频率前k高的元素。
示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]
示例 2:
输入: nums = [1], k = 1
输出: [1]
提示：
你可以假设给定的k总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
你的算法的时间复杂度必须优于 O(n log n) ,n是数组的大小。
题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
你可以按任意顺序返回答案。
'''


class Solution(object):
    def topKFrequent(self, nums, k):
        # 哈希表存储，元素及出现次数
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        # 将哈希表转为二维列表，这里的key如果写成k，在LeetCode上就过不去，浪费了我好多时间
        d_list = [[key, v] for key, v in d.items()]

        def adjustMinHeap(array, i, n):
            tmp = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and array[left][1] < array[tmp][1]:
                tmp = left
            if right < n and array[right][1] < array[tmp][1]:
                tmp = right
            if tmp != i:
                array[tmp], array[i] = array[i], array[tmp]
                adjustMinHeap(array, tmp, n)

        # 建堆，只需要k个元素
        n = len(d_list)
        for i in range((k - 1) // 2, -1, -1):
            adjustMinHeap(d_list, i, k)
        # 剩余依次和堆顶比较
        for i in range(k, n):
            if d_list[i][1] > d_list[0][1]:
                d_list[0] = d_list[i]
                adjustMinHeap(d_list, 0, k)
        res = []
        for i in range(k):
            res.append(d_list[i][0])
        return res


if __name__ == '__main__':
    u = Solution()
    nums1 = [1, 1, 1, 2, 2, 3]
    nums2 = [1]
    print(u.topKFrequent(nums1, 2))
    print(u.topKFrequent(nums2, 1))

'''
给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。
示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：
输入：lists = []
输出：[]
示例 3：
输入：lists = [[]]
输出：[]
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 两两合并链表。时间复杂度O(nlogk)，空间复杂度O(1)，
    def mergeKLists(self, lists):
        # 合并两个升序链表
        def merge(l1, l2):
            cur = dummy = ListNode(0)
            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            cur.next = p1 if p1 else p2
            return dummy.next

        if not lists:
            return None
        length = len(lists)
        if length == 1:
            return lists[0]
        while length > 1:
            idx = 0
            for i in range(0, length, 2):
                if i == length - 1:
                    lists[idx] = lists[i]
                else:
                    # 两两合并
                    lists[idx] = merge(lists[i], lists[i + 1])
                idx += 1
            length = idx
        return lists[0]


if __name__ == '__main__':
    u = Solution()
    l1_1 = ListNode(1)
    l1_4 = l1_1.next = ListNode(4)
    l1_5 = l1_4.next = ListNode(5)
    l2_1 = ListNode(1)
    l2_3 = l2_1.next = ListNode(3)
    l2_4 = l2_3.next = ListNode(4)
    l3_2 = ListNode(2)
    l3_6 = l3_2.next = ListNode(6)

    l_none = ListNode(None)

    list1 = [l1_1, l2_1, l3_2]
    list2 = []
    list3 = [l_none]

    res1 = u.mergeKLists(list1)
    while res1:
        print(res1.val, end='→')
        res1 = res1.next
    print()
    res2 = u.mergeKLists(list2)
    print(res2)
    res3 = u.mergeKLists(list3)
    print(res3)

'''
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 暴力
        res = []
        cur = dummy = ListNode(0)
        for i in lists:
            while i:
                res.append(i.val)
                i = i.next
        for x in sorted(res):
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next

if __name__ == '__main__':
    u = Solution()
    # [[1,4,5],[1,3,4],[2,6]]  -----> [1,1,2,3,4,4,5,6]
    l1_1 = ListNode(1)
    l1_2 = l1_1.next = ListNode(4)
    l1_3 = l1_2.next = ListNode(5)

    l2_1 = ListNode(1)
    l2_2 = l2_1.next = ListNode(3)
    l2_3 = l2_2.next = ListNode(4)

    l3_1 = ListNode(2)
    l3_2 = l3_1.next = ListNode(6)

    l = [l1_1, l2_1, l3_1]
    res = u.mergeKLists(l)
    while res:
        print(res.val, end='→')
        res = res.next


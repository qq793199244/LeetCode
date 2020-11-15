'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
示例：给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明：你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        p = dummy = ListNode(0)
        while True:
            count = k
            stack = []  # 辅助栈
            cur = head
            while count and cur:
                stack.append(cur)
                cur = cur.next
                count -= 1
            if count:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = cur
            head = cur
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)
    l3 = l2.next = ListNode(3)
    l4 = l3.next = ListNode(4)
    l5 = l4.next = ListNode(5)
    res = u.reverseKGroup(l1, k=2)
    while res:
        print(res.val, end='→')
        res = res.next

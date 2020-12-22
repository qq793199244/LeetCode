'''
给定一个链表，删除链表的倒数第n个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：
给定的 n 保证是有效的。
进阶：
你能尝试使用一趟扫描实现吗？
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return head
        length = 0
        i = head
        while i:
            length += 1
            i = i.next
        cur = dummy = ListNode(0)
        cur.next = head
        for i in range(length - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

    def removeNthFromEnd2(self, head, n):
        slow = dummy = ListNode(0)
        slow.next = head
        fast = head
        for _ in range(n):
            # if not fast:
            #     return None
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    head1 = ListNode(1)
    n2 = head1.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    n4 = n3.next = ListNode(4)
    n5 = n4.next = ListNode(5)

    cur = head1
    while cur:
        print(cur.val, end='→')
        cur = cur.next
    print()
    print('----------------------------')

    # res = u.removeNthFromEnd(head1, 4)
    # while res:
    #     print(res.val, end='→')
    #     res = res.next

    res = u.removeNthFromEnd2(head1, 2)
    while res:
        print(res.val, end='→')
        res = res.next

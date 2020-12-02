'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.
当删除了倒数第二个节点后，链表变为 1->2->3->5.
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
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy
        while n > 0:
            fast = fast.next
            n -= 1
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    head = ListNode(1)
    n2 = head.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    n4 = n3.next = ListNode(4)
    n5 = n4.next = ListNode(5)
    while head:
        print(head.val, end='→')
        head = head.next
    print()
    print('----------------------------')
    res = u.removeNthFromEnd2(head, 2)
    while res:
        print(res.val, end='→')
        res = res.next
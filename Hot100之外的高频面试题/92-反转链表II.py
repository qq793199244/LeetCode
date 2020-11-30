'''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
说明:
1 ≤ m ≤ n ≤ 链表长度。
示例:
输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head or not head.next or m==n:
            return head
        cur = dummy = ListNode(0)
        cur.next = head
        for _ in range(m-1):
            cur = cur.next
        h = cur.next
        t = h
        for _ in range(n-m):
            t = t.next
        n_plus1 = t.next
        t.next = None
        def reverseList(head):
            pre, cur = None, head
            while cur:
                tmp = cur.next
                cur.next = pre
                pre = cur
                cur = tmp
            return pre
        cur.next = reverseList(h)
        h.next = n_plus1
        return dummy.next


if __name__ == '__main__':
    u1 = Solution()
    l_1 = ListNode(1)
    l_2 = l_1.next = ListNode(2)
    l_3 = l_2.next = ListNode(3)
    l_4 = l_3.next = ListNode(4)
    l_5 = l_4.next = ListNode(5)

    res = u1.reverseBetween(l_1, 2, 4)
    while res:
        print(res.val, end='→')
        res = res.next
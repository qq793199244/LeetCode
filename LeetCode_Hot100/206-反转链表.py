'''反转一个单链表。
示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

if __name__ == '__main__':
    u1 = Solution()

    l_1 = ListNode(1)
    l_2 = l_1.next = ListNode(2)
    l_3 = l_2.next = ListNode(3)
    l_4 = l_3.next = ListNode(4)
    l_5 = l_4.next = ListNode(5)

    res = u1.reverseList(l_1)
    while res:
        print(res.val, end='→')
        res = res.next
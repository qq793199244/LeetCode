'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dummy =ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dummy.next

if __name__ == '__main__':
    '''
    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    '''
    u1 = Solution()
    l1 = ListNode(1)
    l1_1 = l1.next = ListNode(2)
    l1_2 = l1_1.next = ListNode(4)
    l2 = ListNode(1)
    l2_1 = l2.next = ListNode(3)
    l2_2 = l2_1.next = ListNode(4)
    res = u1.mergeTwoLists(l1, l2)
    while res:
        print(res.val, end='→')
        res = res.next

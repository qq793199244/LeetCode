'''
请判断一个链表是否为回文链表。
示例 1:
输入: 1->2
输出: false
示例 2:
输入: 1->2->2->1
输出: true
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True

        halfTail = self.findHalfTail(head)
        l2_start = self.reverseLinkList(halfTail.next)
        cur1 = head
        cur2 = l2_start
        while cur2:
            if cur2.val != cur1.val:
                return False
            else:
                cur2 = cur2.next
                cur1 = cur1.next
        return True

    # 寻找前半部尾结点
    def findHalfTail(self, head):
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    # 反转链表
    def reverseLinkList(self, head):
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
    l1_h = ListNode(1)
    l1_2 = l1_h.next = ListNode(2)
    res1 = u1.isPalindrome(l1_h)
    print(res1)

    u2 = Solution()
    l2_h = ListNode(1)
    l2_2 = l2_h.next = ListNode(2)
    l2_3 = l2_2.next = ListNode(2)
    l2_4 = l2_3.next = ListNode(1)
    res2 = u2.isPalindrome(l2_h)
    print(res2)
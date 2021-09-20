'''
编写一个函数，检查输入的链表是否是回文的。
示例 1：
输入： 1->2
输出： false
示例 2：
输入： 1->2->2->1
输出： true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
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
    u = Solution()
    l1 = ListNode(1)
    l1_n2 = l1.next = ListNode(2)

    l2 = ListNode(1)
    l2_n2 = l2.next = ListNode(2)
    l2_n3 = l2_n2.next = ListNode(2)
    l2_n4 = l2_n3.next = ListNode(1)

    print(u.isPalindrome(l1))  # False
    print(u.isPalindrome(l2))  # True

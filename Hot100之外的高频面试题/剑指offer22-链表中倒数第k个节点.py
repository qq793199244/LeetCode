'''
输入一个链表，输出该链表中倒数第k个节点。
为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。
这个链表的倒数第3个节点是值为4的节点。
示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 不用算链的总长度
    def getKthFromEnd(self, head, k):
        if not head or k == 0:
            return None
        fast = slow = head
        # 快指针比慢指针先走k-1步，0至k-1是走了k-1步
        for _ in range(k):
            # k大于链表长度的情况
            if not fast:
                return None
            fast = fast.next
        # 同时走
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    # 算链的长度
    def getKthFromEnd2(self, head, k):
        if not head:
            return None
        i = cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if k > count:
            return None
        for _ in range(count - k):
            i = i.next
        return i


if __name__ == '__main__':
    u = Solution()
    '''给定一个链表: 1->2->3->4->5, 和 k = 2. 返回链表 4->5.'''
    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)
    l3 = l2.next = ListNode(3)
    l4 = l3.next = ListNode(4)
    l5 = l4.next = ListNode(5)

    res = u.getKthFromEnd(l1, 2)
    while res:
        print(res.val, end='→')
        res = res.next
    print()
    res2 = u.getKthFromEnd(l1, 7)
    print(res)


    f1 = u.getKthFromEnd2(l1, 2)
    while f1:
        print(f1.val, end='→')
        f1 = f1.next
    print()
    f2 = u.getKthFromEnd2(l1, 7)
    while f2:
        print(f2.val, end='→')
        f2 = f2.next

'''
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
注意：本题相对原题稍作改动
示例：
输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：
给定的 k 保证是有效的。
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 常规想法，遍历两次。时间复杂度O(n)，空间复杂度O(1)
    def kthToLast(self, head, k):
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        p = head
        for i in range(count - k):
            p = p.next
        return p.val

    # 双指针。时间复杂度O(n)，空间复杂度O(1)
    def kthToLast2(self, head, k):
        cur = pre = head
        for i in range(k):
            cur = cur.next
        while cur:
            cur, pre = cur.next, pre.next
        return pre.val


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    n2 = l1.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    n4 = n3.next = ListNode(4)
    n5 = n4.next = ListNode(5)
    print(u.kthToLast(l1, 2))  # 4
    print(u.kthToLast2(l1, 2))  # 4

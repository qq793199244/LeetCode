'''
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
示例 1：
输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：
输入：head = [0,1,2], k = 4
输出：[2,0,1]
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 时间复杂度O(n)，空间复杂度O(1)
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head
        # 添加一个伪头结点
        cur = p = dummy = ListNode(0)
        dummy.next = head
        # 计算共有多少个节点
        count = 0
        while cur.next:
            cur = cur.next
            count += 1
        # 实际移动多少位
        k = k % count
        if k == 0:
            return head
        # 找新尾结点位置
        tail = count - k
        while p:
            p = p.next
            tail -= 1
            if tail == 0:
                break
        dummy.next = p.next  # 新尾结点后的节点为新的头节点
        p.next = None  # 断链
        cur.next = head  # 原尾节点与原头节点连接
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    l1_n2 = l1.next = ListNode(2)
    l1_n3 = l1_n2.next = ListNode(3)
    l1_n4 = l1_n3.next = ListNode(4)
    l1_n5 = l1_n4.next = ListNode(5)
    res1 = u.rotateRight(l1, 2)
    while res1:
        print(res1.val, end='→')
        res1 = res1.next

    print()

    l2 = ListNode(0)
    l2_n1 = l2.next = ListNode(1)
    l2_n2 = l2_n1.next = ListNode(2)
    res2 = u.rotateRight(l2, 4)
    while res2:
        print(res2.val, end='→')
        res2 = res2.next

    print()

    l3 = ListNode(1)
    l3_2 = l3.next = ListNode(2)
    res3 = u.rotateRight(l3, 2)
    while res3:
        print(res3.val, end='→')
        res3 = res3.next

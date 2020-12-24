'''
给你一个链表，每k个节点一组进行翻转，请你返回翻转后的链表。
k是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是k的整数倍，那么请将最后剩余的节点保持原有顺序。
示例：给你这个链表：1->2->3->4->5
当k= 2 时，应当返回: 2->1->4->3->5
当k= 3 时，应当返回: 3->2->1->4->5
说明：你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        p = dummy = ListNode(0)
        while True:
            count = k
            stack = []  # 辅助栈
            cur = head
            # 进栈，进count个，且节点不为空
            while count and cur:
                stack.append(cur)
                cur = cur.next
                count -= 1
            # 如果剩下的一组不满k个
            if count:
                p.next = head
                break
            # 出栈，连接
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = cur
            head = cur
        return dummy.next

    def reverseKGroup2(self, head, k):
        if not head or k <= 0:
            return head
        dummy = ListNode(0)
        p = dummy
        dummy.next = head
        count = k
        # 反转单个链表
        def reverse(head):
            pre = None
            cur = head
            while cur:
                t = cur.next
                cur.next = pre
                pre = cur
                cur = t
            return pre
        # 增加一个哨兵节点，之后不断遍历链表
        while p.next:
            tmp = p
            # 遍历得到k个长度的链表
            while tmp and tmp.next and count > 0:
                tmp = tmp.next
                count -= 1
            # 如果遍历后的链表长度不满k，则不满足反转条件
            if count != 0:
                break
            # 如果count==0说明符合条件，就反转这一组链表
            else:
                # 反转之前需要将下一个节点保存，并设置next为空，防止循环指向
                next_node = tmp.next
                tail = p.next
                tmp.next = None
                # 假设链表为1->2->3->4，下面的nextNode就是4，tail是1
                p.next = reverse(tail)
                tail.next = next_node
                p = tail
                count = k
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    l2 = l1.next = ListNode(2)
    l3 = l2.next = ListNode(3)
    l4 = l3.next = ListNode(4)
    l5 = l4.next = ListNode(5)

    # res1 = u.reverseKGroup(l1, k=2)
    # while res1:
    #     print(res1.val, end='→')
    #     res1 = res1.next

    print()

    res2 = u.reverseKGroup2(l1, k=2)
    while res2:
        print(res2.val, end='→')
        res2 = res2.next

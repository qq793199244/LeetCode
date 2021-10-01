'''
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：
输入：head = []
输出：[]
示例 3：
输入：head = [1]
输出：[1]
提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 时间复杂度O(n)，空间复杂度O(1)
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        tmp = dummy
        while tmp.next and tmp.next.next:
            n1 = tmp.next
            n2 = tmp.next.next
            tmp.next = n2
            n1.next = n2.next
            n2.next = n1
            tmp = n1
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    n2 = l1.next = ListNode(2)
    n3 = n2.next = ListNode(3)
    n4 = n3.next = ListNode(4)

    res = u.swapPairs(l1)
    while res:
        print(res.val, end='→')
        res = res.next


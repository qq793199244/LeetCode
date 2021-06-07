'''
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。
题目数据 保证 整个链式结构中不存在环。
注意，函数返回结果后，链表必须 保持其原始结构 。
示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 双指针。时间复杂度O(m+n)，空间复杂度O(1)
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1


if __name__ == '__main__':
    u = Solution()
    A1 = ListNode(4)
    A1n1 = A1.next = ListNode(1)
    A1n8 = A1n1.next = ListNode(8)
    A1n4 = A1n8.next = ListNode(4)
    A1n5 = A1n4.next = ListNode(5)

    B1 = ListNode(5)
    B1n0 = B1.next = ListNode(0)
    B1n1 = B1n0.next = ListNode(1)
    B1n8 = B1n1.next = ListNode(8)
    B1n4 = B1n8.next = A1n4
    B1n5 = B1n4.next = A1n5
    print(u.getIntersectionNode(A1, B1).val)

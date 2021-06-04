'''
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
示例 1：
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
示例 2：
输入：l1 = [], l2 = []
输出：[]
示例 3：
输入：l1 = [], l2 = [0]
输出：[0]
提示：
两个链表的节点数目范围是 [0, 50]
-100 <= Node.val <= 100
l1 和 l2 均按 非递减顺序 排列
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 时间复杂度O(m+n)，空间复杂度O(1)
    def mergeTwoLists(self, l1, l2):
        cur = dummy = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1: cur.next = l2
        if not l2: cur.next = l1
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    u1_l1 = ListNode(1)
    u1_n2 = u1_l1.next = ListNode(2)
    u1_n4 = u1_n2.next = ListNode(4)
    u1_l2 = ListNode(1)
    u1_2n3 = u1_l2.next = ListNode(3)
    u1_2n4 = u1_2n3.next = ListNode(4)
    res1 = u.mergeTwoLists(u1_l1, u1_l2)
    print('res1:', res1)
    while res1:
        print(res1.val, end='→')
        res1 = res1.next

    print('-----------------------------------')
    u2_l1 = None
    u2_l2 = None
    res2 = u.mergeTwoLists(u2_l1, u2_l2)
    print('res2:', res2)
    while res2:
        print(res2.val, end='→')
        res2 = res2.next

    print('-----------------------------------')
    u3_l1 = None
    u3_l2 = ListNode(0)
    res3 = u.mergeTwoLists(u3_l1, u3_l2)
    print('res3:', res3)
    while res3:
        print(res3.val, end='→')
        res3 = res3.next

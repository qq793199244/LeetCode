'''
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
输入：head = [1,2]
输出：[2,1]
示例 3：
输入：head = []
输出：[]
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 时间复杂度O(n)，空间复杂度O(1)
    def reverseList(self, head):
        cur = head
        pre = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    u = Solution()
    head1 = ListNode(1)
    h1_2 = head1.next = ListNode(2)
    h1_3 = h1_2.next = ListNode(3)
    h1_4 = h1_3.next = ListNode(4)
    h1_5 = h1_4.next = ListNode(5)
    res1 = u.reverseList(head1)
    while res1:
        print(res1.val, end="→")
        res1 = res1.next
    print()
    print('---------------------------------')

    head2 = ListNode(1)
    h2_2 = head2.next = ListNode(2)
    res2 = u.reverseList(head2)
    while res2:
        print(res2.val, end="→")
        res2 = res2.next
    print()
    print('---------------------------------')

    head3 = ListNode(None)
    res3 = u.reverseList(head3)
    while res3:
        print(res3.val, end="→")
        res3 = res3.next
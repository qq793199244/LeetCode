'''
请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点。传入函数的唯一参数为 要被删除的节点 。
示例 1：
输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2：
输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
提示：
链表至少包含两个节点。
链表中所有节点的值都是【唯一】的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
【不要从你的函数中返回任何结果。】
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 直接操作，不要想复杂。时间复杂度O(1)，空间复杂度O(1)
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    u = Solution()
    node = ListNode(4)
    n5 = node.next = ListNode(5)
    n1 = n5.next = ListNode(1)
    n9 = n1.next = ListNode(9)

    cur = node
    while cur:
        print(cur.val, end='→')
        cur = cur.next

    print()
    u.deleteNode(n5)
    while node:
        print(node.val, end='→')
        node = node.next

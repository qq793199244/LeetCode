'''
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        dummy = ListNode(0)
        s = 0
        while stack1 or stack2 or s:
            s1 = stack1.pop() if stack1 else 0
            s2 = stack2.pop() if stack2 else 0
            cur = s1 + s2 + s
            s = 1 if cur >= 10 else 0
            cur = cur % 10
            curNode = ListNode(cur)
            curNode.next = dummy.next
            dummy.next = curNode
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(7)
    l1_node2 = l1.next = ListNode(2)
    l1_node4 = l1_node2.next = ListNode(4)
    l1_node3 = l1_node4.next = ListNode(3)
    l2 = ListNode(5)
    l2_node6 = l2.next = ListNode(6)
    l2_node4 = l2_node6.next = ListNode(4)
    res = u.addTwoNumbers(l1, l2)
    while res:
        print(res.val, end='')
        res = res.next
'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例 1：
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：
输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]
提示：
每个链表中的节点数在范围 [1, 100] 内
0 <= Node.val <= 9
题目数据保证列表表示的数字不含前导零
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    # 时间复杂度O(max(m, n))，空间复杂度O(1)
    def addTwoNumbers(self, l1, l2):
        cur = dummy = ListNode(0)  # 创建伪头节点
        s = 0  # 进位数初始为0
        while l1 or l2 or s:  # l1为空 或 l2为空 或 进位数为0
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + s  # 当前数s = 当前l1 + 当前l2 + 进位数s
            cur.next = ListNode(s % 10)  # 当前位剩的数
            cur = cur.next  # 移动指针
            s = s // 10  # 进位数
            l1 = l1.next if l1 else None  # l1移动指针
            l2 = l2.next if l2 else None  # l2移动指针
        return dummy.next  # 返回伪头节点的下一个节点


if __name__ == '__main__':
    u = Solution()
    l1_1 = ListNode(2)
    l1_2 = l1_1.next = ListNode(4)
    l1_3 = l1_2.next = ListNode(3)
    l2_1 = ListNode(5)
    l2_2 = l2_1.next = ListNode(6)
    l2_3 = l2_2.next = ListNode(4)
    res = u.addTwoNumbers(l1_1, l2_1)
    while res:
        print(res.val, end='→')
        res = res.next

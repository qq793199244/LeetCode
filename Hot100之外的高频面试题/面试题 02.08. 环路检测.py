'''
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。若环不存在，请返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。
进阶：
你是否可以不用额外空间解决此题？
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and fast == slow:
                p = head
                while p != slow:
                    p = p.next
                    slow = slow.next
                return p
        return None


if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(3)
    l1_n2 = l1.next = ListNode(2)
    l1_n0 = l1_n2.next = ListNode(0)
    l1_n4 = l1_n0.next = ListNode(-4)
    l1_n4.next = l1_n2
    print(u.detectCycle(l1).val)
    l2 = ListNode(1)
    l2_n2 = l2.next = ListNode(2)
    l2_n2.next = l2
    print(u.detectCycle(l2).val)
    l3 = ListNode(1)
    print(u.detectCycle(l3))
'''
给定一个链表，判断链表中是否有环。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
如果链表中存在环，则返回 true 。 否则，返回 false 。
进阶：
你能用 O(1)（即，常量）内存解决此问题吗？
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针。时间复杂度O(n)，空间复杂度O(1)
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        fast = head.next
        slow = head
        while fast != slow:
            if not fast or not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
        return True


if __name__ == '__main__':
    u = Solution()
    h1 = ListNode(3)
    h1_2 = h1.next = ListNode(2)
    h1_0 = h1_2.next = ListNode(0)
    h1__4 = h1_0.next = ListNode(-4)
    h1__4.next = h1_2
    print(u.hasCycle(h1))  # True

    h2 = ListNode(1)
    h2_2 = h2.next = ListNode(2)
    h2_2.next = h2
    print(u.hasCycle(h2))  # True

    h3 = ListNode(1)
    print(u.hasCycle(h3))  # False

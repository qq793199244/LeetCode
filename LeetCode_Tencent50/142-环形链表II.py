'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
说明：不允许修改给定的链表。
进阶：你是否可以使用 O(1) 空间解决此题？
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 快慢指针。时间复杂度O(n)，空间复杂度O(1)
    def EntryNodeOfLoop(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        slow = fast = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast and fast == slow:
                fast = pHead
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None

    # 哈希表。时间复杂度O(n)，空间复杂度O(n)
    def EntryNodeOfLoop2(self, pHead):
        if not pHead or not pHead.next or not pHead.next.next:
            return None
        hash = set()
        while pHead:
            if pHead not in hash:
                hash.add(pHead)
                pHead = pHead.next
            else:
                return pHead


if __name__ == '__main__':
    u = Solution()
    h1 = ListNode(3)
    h1_2 = h1.next = ListNode(2)
    h1_0 = h1_2.next = ListNode(0)
    h1__4 = h1_0.next = ListNode(-4)
    h1__4.next = h1_2

    h2 = ListNode(1)
    h2_2 = h2.next = ListNode(2)
    h2_2.next = h2

    h3 = ListNode(1)

    print(u.EntryNodeOfLoop(h1))
    print(u.EntryNodeOfLoop2(h1))

    print(u.EntryNodeOfLoop(h2))
    print(u.EntryNodeOfLoop2(h2))

    print(u.EntryNodeOfLoop(h3))
    print(u.EntryNodeOfLoop2(h3))


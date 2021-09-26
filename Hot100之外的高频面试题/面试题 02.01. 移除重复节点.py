'''
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。
示例1:
 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:
 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：
链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。
进阶：
如果不得使用临时缓冲区，该怎么解决？
'''


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 利用集合去重。时间复杂度O(n)，空间复杂度O(n)
    def removeDuplicateNodes(self, head):
        cur = head
        pre = ListNode(-1)
        pre.next = head
        nodes = set()
        while cur:
            if cur.val not in nodes:
                nodes.add(cur.val)
                pre, cur = pre.next, cur.next
            else:
                cur = cur.next
                pre.next = cur
        return head

if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(1)
    l1_n2 = l1.next = ListNode(1)
    l1_n3 = l1_n2.next = ListNode(1)
    l1_n4 = l1_n3.next = ListNode(1)
    l1_n5 = l1_n4.next = ListNode(2)
    cur = l1
    while cur:
        print(cur.val, end='→')
        cur = cur.next
    u.removeDuplicateNodes(l1)
    print()
    cur = l1
    while cur:
        print(cur.val, end='→')
        cur = cur.next



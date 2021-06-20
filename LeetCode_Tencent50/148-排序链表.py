'''
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
进阶：
你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
示例 1：
输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：
输入：head = []
输出：[]
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    # 归并排序。时间复杂度O(nlogn)，空间复杂度O(1)
    def sortList(self, head):
        # 合并两个有序链表
        def merge(l1, l2):
            cur = dummy = ListNode(0)
            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val < p2.val:
                    cur.next = p1
                    p1 = p1.next
                else:
                    cur.next = p2
                    p2 = p2.next
                cur = cur.next
            cur.next = p1 if p1 else p2
            return dummy.next

        if not head or not head.next:
            return head
        # 统计链表长度
        length = 0
        count = head
        while count:
            length += 1
            count = count.next
        dummy = ListNode(0, head)
        # 设置切片大小
        subLength = 1
        while subLength < length:
            pre, cur = dummy, dummy.next
            # 根据当前的合并规模，将链表内的链表切片两两归并
            while cur:
                # 获取当前需要合并的子链表head1
                head1 = cur
                for i in range(1, subLength):
                    if cur.next:
                        cur = cur.next
                    else:
                        break
                # 获取当前需要合并的子链表head2
                head2 = cur.next
                cur.next = None  # 断链
                cur = head2
                for i in range(1, subLength):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                succ = None
                if cur:
                    succ = cur.next
                    cur.next = None
                merged = merge(head1, head2)
                pre.next = merged
                while pre.next:
                    pre = pre.next
                cur = succ
            subLength *= 2
        return dummy.next


if __name__ == '__main__':
    u = Solution()
    h1 = ListNode(4)
    h1_2 = h1.next = ListNode(2)
    h1_1 = h1_2.next = ListNode(1)
    h1_3 = h1_1.next = ListNode(3)

    h2 = ListNode(-1)
    h2_5 = h2.next = ListNode(5)
    h2_3 = h2_5.next = ListNode(3)
    h2_4 = h2_3.next = ListNode(4)
    h2_0 = h2_4.next = ListNode(0)

    h3 = ListNode(None)

    res1 = u.sortList(h1)
    while res1:
        print(res1.val, end='→')
        res1 = res1.next
    print()
    res2 = u.sortList(h2)
    while res2:
        print(res2.val, end='→')
        res2 = res2.next
    print()
    res3 = u.sortList(h3)
    print(res3)

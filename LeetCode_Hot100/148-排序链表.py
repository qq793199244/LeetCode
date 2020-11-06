'''
给你链表的头结点head，请将其按升序排列并返回排序后的链表。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        cur, intv, length = head, 1, 0
        # 统计链表长度
        while cur:
            length += 1
            cur = cur.next
        # 添伪头结点
        dummy = ListNode(0)
        dummy.next = head
        # 根据不同的链表切片规模，每一次都从头进行归并
        while intv < length:
            merge_point = dummy
            cur = dummy.next
            # 根据当前的合并规模，将链表内的链表切片两两归并
            while cur:
                # 获取当前需要归并的子链表l1
                l1 = cur
                intv_re1 = intv
                while intv_re1 and cur:
                    cur = cur.next
                    intv_re1 -= 1
                if intv_re1:
                    break
                # 获取当前需要归并的子链表l2
                l2 = cur
                intv_re2 = intv
                while intv_re2 and cur:
                    cur = cur.next
                    intv_re2 -= 1
                len1, len2 = intv, intv - intv_re2
                # 归并排序
                while len1 and len2:
                    if l1.val < l2.val:
                        merge_point.next = l1
                        l1 = l1.next
                        len1 -= 1
                    else:
                        merge_point.next = l2
                        l2 = l2.next
                        len2 -= 1
                    merge_point = merge_point.next
                # 处理多余剩下的
                if len1:
                    merge_point.next = l1
                else:
                    merge_point.next = l2
                while len1 > 0 or len2 > 0:
                    merge_point = merge_point.next
                    len1 -= 1
                    len2 -= 1
                '''
                l1和l2的归并只是影响了链表的一部分，
                这里应该把归并后的链表切片跟原链表l2之后的部分拼起来 '''
                merge_point.next = cur
            intv *= 2
        return dummy.next

if __name__ == '__main__':
    u = Solution()
    l1 = ListNode(5)
    l2 = l1.next = ListNode(4)
    l3 = l2.next = ListNode(3)
    l4 = l3.next = ListNode(2)
    l5 = l4.next = ListNode(1)
    res = u.sortList(l1)
    while res:
        print(res.val, end='→')
        res = res.next




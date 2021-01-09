'''
运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value)如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶：你是否可以在O(1) 时间复杂度内完成这两种操作？
示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]
解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
提示：
1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put
'''


# 先定义一个双向链表
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        # 如果当前key已经存在字典中，把这个节点移到链表末尾
        if key in self.dic:
            self._remove(self.dic[key])
            node = ListNode(key, value)
            self._add(node)
            self.dic[key] = node
        # 如果在字典中未出现过
        else:
            # 判断当前容量是否已满，如果满了，先删除head节点后的节点，即最久未使用的那个节点，字典中也要删
            if len(self.dic) == self.capacity:
                node_del = self.head.next
                del self.dic[node_del.key]
                self._remove(node_del)
            # 然后插入新节点
            node = ListNode(key, value)
            self._add(node)
            self.dic[key] = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        # 让新来的这个node插入在p和tail之间
        p = self.tail.prev
        p.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = p


if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)
    '''输入["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
            [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
        输出[null, null, null, 1, null, -1, null, -1, 3, 4]
    '''
    print(obj)
    print(obj.put(1, 1))
    print(obj.put(2, 2))
    print(obj.get(1))
    print(obj.put(3, 3))
    print(obj.get(2))
    print(obj.put(4, 4))
    print(obj.get(1))
    print(obj.get(3))
    print(obj.get(4))

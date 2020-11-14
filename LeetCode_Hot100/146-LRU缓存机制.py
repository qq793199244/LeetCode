'''
运用你所掌握的数据结构，设计和实现一个 LRU (Least Recently Used最近最少使用) 缓存机制 。
实现 LRUCache 类：
LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
复杂度分析
时间复杂度：对于 put 和 get 都是 O(1)。
空间复杂度：O(capacity)，因为哈希表和双向链表最多存储capacity+1个元素。

'''


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # 两个伪头尾节点
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        # 若key在字典中，将这个节点放到链表结尾（伪尾结点之前）
        if key in self.dic:
            node = self.dic[key]
            # 先把原位置的删掉
            self._remove(node)
            # 再放到结尾
            self._add(node)
            return node.val
        return -1

    def put(self, key, val):
        node = Node(key, val)
        if key in self.dic:
            self._remove(self.dic[key])
        self._add(node)
        self.dic[key] = node
        if len(self.dic) > self.capacity:
            node_del = self.head.next
            del self.dic[node_del.key]
            self._remove(node_del)



    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node


if __name__ == '__main__':
    u = LRUCache(2)
    '''
    输入["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    输出[null, null, null, 1, null, -1, null, -1, 3, 4]
'''
    print(u)
    print(u.put(1, 1))
    print(u.put(2, 2))
    print(u.get(1))
    print(u.put(3, 3))
    print(u.get(2))
    print(u.put(4, 4))
    print(u.get(1))
    print(u.get(3))
    print(u.get(4))

'''
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（push、pop、peek、empty）：
实现 MyQueue 类：
void push(int x) 将元素 x 推到队列的末尾
int pop() 从队列的开头移除并返回元素
int peek() 返回队列开头的元素
boolean empty() 如果队列为空，返回 true ；否则，返回 false
说明：
你只能使用标准的栈操作 —— 也就是只有push to top,peek/pop from top,size, 和is empty操作是合法的。
你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
进阶：
你能否实现每个操作均摊时间复杂度为 O(1) 的队列？
换句话说，执行 n 个操作的总时间复杂度为 O(n) ，即使其中一个操作可能花费较长时间。
示例：
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]
解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
提示：
1 <= x <= 9
最多调用 100 次 push、pop、peek 和 empty
假设所有操作都是有效的 （例如，一个空的队列不会调用 pop 或者 peek 操作）
'''


class MyQueue(object):

    def __init__(self):
        # s1用来反转元素的入队顺序，s2用来存储元素的最终顺序
        self.s1 = []
        self.s2 = []
        self.front = None

    def push(self, x):      # 时间复杂度O(1)；空间复杂度O(n)
        # 新元素总是压入s1的栈顶，同时把s1中压入的第一个元素赋值给作为队首元素的front变量
        if not self.s1:
            self.front = x
        self.s1.append(x)

    def pop(self):      # 摊还时间复杂度O(1)，最坏情况下的时间复杂度O(n)；空间复杂度O(1)
        # 摊还分析给出了所有操作的平均性能。
        # 摊还分析的核心在于，最坏情况下的操作一旦发生了一次，那么在未来很长一段时间都不会再次发生，这样就会均摊每次操作的代价。
        # 如果s2中为空，把s1中元素反转到s2中
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            # 当s1中空了，front置空
            self.front = None
        return self.s2.pop()

    def peek(self):     # 时间复杂度O(1)；空间复杂度O(1)
        # 如果s2中还有元素，那么s2栈顶元素就是队首元素；否则直接返回front
        if self.s2:
            return self.s2[-1]
        return self.front

    def empty(self):    # 时间复杂度O(1)；空间复杂度O(1)
        # 如果两个栈都为空，那么队列为空；否则队列不为空
        if not self.s1 and not self.s2:
            return True
        return False


if __name__ == '__main__':
    # 输入
    #["MyQueue", "push", "push", "peek", "pop", "empty"]
    #[[], [1], [2], [], [], []]
    # 输出
    # None None None 1 1 False
    my_queue = MyQueue()
    print(my_queue.__init__(), end=' ')
    print(my_queue.push(1), end=' ')
    print(my_queue.push(2), end=' ')
    print(my_queue.peek(), end=' ')
    print(my_queue.pop(), end=' ')
    print(my_queue.empty(), end=' ')

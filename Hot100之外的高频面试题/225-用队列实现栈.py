'''
使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:
你只能使用队列的基本操作-- 也就是push to back, peek/pop from front, size, 和is empty这些操作是合法的。
你所使用的语言也许不支持队列。你可以使用 list 或者 deque（双端队列）来模拟一个队列, 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
'''


# 时间复杂度，入栈操作O(n)，其他O(1)；空间复杂度O(n)
class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):
        # 先把元素push进q2
        self.q2.append(x)
        # 如果q1不为空，把q1中最左边的元素添加到q2，直到q1为空
        while self.q1:
            self.q2.append(self.q1.pop(0))
        # q1和q2交换，元素都在q1中，现在q2为空
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop(0)

    def top(self):
        return self.q1[0]

    def empty(self):
        if not self.q1:
            return True
        return False


if __name__ == '__main__':
    my_stack = MyStack()
    # 输入
    # ["MyStack","push","push","top","pop","empty"]
    # [[],[1],[2],[],[],[]]
    # 输出
    # [null,null,null,2,2,false]
    print(my_stack.__init__(), end=' ')
    print(my_stack.push(1), end=' ')
    print(my_stack.push(2), end=' ')
    print(my_stack.top(), end=' ')
    print(my_stack.pop(), end=' ')
    print(my_stack.empty(), end=' ')

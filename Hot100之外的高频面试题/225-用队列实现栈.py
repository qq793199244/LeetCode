'''
使用队列实现栈的下列操作：
push(x) -- 元素 x 入栈
pop() -- 移除栈顶元素
top() -- 获取栈顶元素
empty() -- 返回栈是否为空
注意:
你只能使用队列的基本操作-- 也就是 push to back, peek/pop from front, size, 和 is empty 这些操作是合法的。
你所使用的语言也许不支持队列。 你可以使用 list 或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
你可以假设所有操作都是有效的（例如, 对一个空的栈不会调用 pop 或者 top 操作）。
'''

class MyStack(object):

    def __init__(self):
        self.q1 = []
        self.q2 = []
        self.front = None

    def push(self, x):  # O(1)
        self.q1.append(x)
        self.front = x

    def pop(self):  #O(n)
         # 把q1里的元素取出，留下一个，其余放入q2中
        for i in range (len(self.q1)-1):
            self.front = self.q1.pop(0)
            self.q2.append(self.front)
        popElement = self.q1.pop(0)
        self.q1 = self.q2
        self.q2 = []
        return popElement

    def top(self):  # O(1)
        return self.front

    def empty(self):    # O(1)
        if not self.q1:
            return True
        return False


if __name__ == '__main__':
    u = MyStack()
    '''
    ["MyStack","push","push","top","pop","empty"]
    [[],[1],[2],[],[],[]]
    [null,null,null,2,2,false]
    '''
    print(u.__init__())
    print(u.push(1))
    print(u.push(2))
    print(u.top())
    print(u.pop())
    print(u.empty())

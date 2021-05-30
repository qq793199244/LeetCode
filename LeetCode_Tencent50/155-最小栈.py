'''
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) —— 将元素 x 推入栈中。
pop()—— 删除栈顶的元素。
top()—— 获取栈顶元素。
getMin() —— 检索栈中的最小元素。
示例:
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
输出：[null,null,null,null,-3,null,0,-2]
解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
提示：
pop、top 和 getMin 操作总是在 非空栈 上调用。
'''


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]


class MinStack2:
    # 如果不使用辅助空间，不用辅助栈。思路是栈里保存差值。
    def __init__(self):
        self.stack = []
        self.min_value = -1

    def push(self, x):
        if not self.stack:
            self.stack.append(0)
            self.min_value = x
        else:
            diff = x - self.min_value
            self.stack.append(diff)
            self.min_value = self.min_value if diff > 0 else x

    def pop(self):
        if self.stack:
            diff = self.stack.pop()
            if diff < 0:
                top = self.min_value
                self.min_value = top - diff
            else:
                top = self.min_value + diff
            return top

    def top(self):
        return self.min_value if self.stack[-1] < 0 else self.stack[-1] + self.min_value

    def getMin(self):
        return self.min_value if self.stack else -1


if __name__ == '__main__':
    # 输入
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # x = [[],[-2],[0],[-3],[],[],[],[]]
    # 输出[null,null,null,null,-3,null,0,-2]
    obj1 = MinStack()
    print(obj1.stack, end=' ')
    print(obj1.getMin(), end=' ')
    print(obj1.push(-2), end=' ')
    print(obj1.push(0), end=' ')
    print(obj1.push(-3), end=' ')
    print(obj1.getMin(), end=' ')
    print(obj1.pop(), end=' ')
    print(obj1.top(), end=' ')
    print(obj1.getMin())
    print('--------------------')
    u = MinStack2()
    obj2 = MinStack()
    print(obj2.stack, end=' ')
    print(obj2.getMin(), end=' ')
    print(obj2.push(-2), end=' ')
    print(obj2.push(0), end=' ')
    print(obj2.push(-3), end=' ')
    print(obj2.getMin(), end=' ')
    print(obj2.pop(), end=' ')
    print(obj2.top(), end=' ')
    print(obj2.getMin())

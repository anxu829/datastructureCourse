# -*- coding:utf-8 -*-

# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。

# 本题的核心是维护一个递减栈

class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack :
            # 若辅助栈内容为空， 则 对辅助栈进行压栈
            self.min_stack.append(node)
        else:
            # 否则压入栈顶元素和node的较小值
            self.min_stack.append(min(node,self.min_stack[-1]))
            
    def pop(self):
        if not self.stack:
            self.stack.pop()
            self.min_stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.min_stack[-1]

if __name__ == '__main__':
    
    # case 1 ["PSH3","MIN","PSH4","MIN","PSH2","MIN","PSH3","MIN","POP","MIN","POP","MIN","POP","MIN","PSH0","MIN"]
    temp = Solution()
    temp.push(3)
    temp.min()
    temp.push(4)
    temp.min()
    temp.push(2)
    temp.min()
    temp.push(3)
    temp.min()
    temp.pop()
    temp.min()
    temp.pop()
    temp.min()

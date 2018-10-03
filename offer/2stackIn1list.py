# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if self.stack2 == []:
            if self.stack1 == []:
                return None
            else:
                for i in range(len(self.stack1)-1, -1, -1):
                    self.stack2.append(self.stack1[i])
                self.stack1 = []
                return self.stack2.pop()
        else:
            return self.stack2.pop()

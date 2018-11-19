# -*- coding:utf-8 -*-

# 要点：利用队列存储中间结果
# 错误案例： 要考虑树为空的特殊情形

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root == None：
            return []
        queue = [root]
        res = []
        while(queue != []):
            # 获取队列尾部的数据
            front = queue[0]
            if front.left !=None:
                queue.append(front.left)
            if front.right !=None:
                queue.append(front.right)
            # 从队列的头部 pop 出数据
            res.append(queue[0].val)
            queue.pop(0)
        return res 

# -*- coding:utf-8 -*-
'''
#题目描述
# 输入一个链表，反转链表后，输出新链表的表头。

# 大体思路：
# 如果是叶节点：则 直接返回
# 如果是非叶节点：则对左右节点各自先做交换，然后交换左右节点
# 【注意】如果二叉树左节点有值，右节点没有值，即函数的输入可能是None
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回ListNode
    def Mirror(self, pHead):
        # 如果返回值是None
        if pHead == None:
            return pHead
        # 如果pHead 是叶节点
        if pHead.left == None and pHead.right == None:
            return pHead
        # 现在pHead 不是叶节点
        t1 = self.Mirror(pHead.left)
        t2 = self.Mirror(pHead.right)
        pHead.right = t1
        pHead.left  = t2
        return pHead

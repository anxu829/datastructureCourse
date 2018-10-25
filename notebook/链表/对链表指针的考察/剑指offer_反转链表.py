
#-*- coding:utf-8 -*-
'''
输入一个链表，反转链表后，输出新链表的表头。

# 首先判断特殊情况：
    # 1 首节点就是空的情况

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self, pHead):
        # 如果节点为 空值：
        if pHead == None:
            
            return None
        # 如果节点 为 两个点：
        if pHead.next != None and pHead.next.next == None:
            node = pHead.next
            node.next = pHead
            node.next.next = None
            return node
        
        




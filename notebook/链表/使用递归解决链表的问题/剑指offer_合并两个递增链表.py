# -*- coding:utf-8 -*-
# 这个题真的最难的点在于：你是想不到优先使用递归的

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None :
            return pHead1
        # 现在pHead1 和 pHead2 都有值
        
        head = ListNode(-1)
        cur  = head
        while(pHead1 != None and pHead2 != None):
            # 两边都有的话
            if pHead1.val <= pHead2.val :
                cur.next = pHead1
                pHead1 = pHead1.next 
            else:
                cur.next = pHead2
                pHead2 = pHead2.next 
            cur = cur.next 
        # 肯定会有一个已经循环完另一个 还没有
        if pHead1 == None:
            cur.next = pHead2
        if pHead2 == None:
            cur.next = pHead1
        return head.next


    def Merge2(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val >= pHead2.val:
            curHead = pHead1
            curHead.next = self.Merge(pHead1.next,pHead2)
        else:
            curHead = pHead2
            curHead.next = self.Merge(pHead1,pHead2.next)

        return curHead

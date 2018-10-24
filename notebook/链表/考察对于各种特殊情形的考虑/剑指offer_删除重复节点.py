#-*- coding:utf-8 -*-
"""
# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
# 返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5



        
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
nums = [1,1,1,1,1,1,2]
pHead = ListNode(1)
nxt = pHead
for i in nums[1:]:
    node  = ListNode(i)
    nxt.next = node 
    nxt = node

class Solution:
    def deleteDuplication(self, pHead):
        # 建立一个listNode
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None
        # 为了统一分析，加入头节点
        # 加入一个头节点 
        if pHead == None:
            return None
        head = ListNode(-1)
        head.next = pHead

        # 拿到节点 
        cur = head
        # 完成移动和删除
        # 核心思路：
            # 判断他下一个和下下个是否是相同的，若有则删除
            # 删干净后，cur向前移动一个单位
        # 异常处理：
            # cur 没有下一个
            # cur 没有下两个
        while(True):
            if cur.next == None or cur.next.next == None:
                break
            start = cur.next
            end = cur.next.next 
            if start.val != end.val:
                cur = cur.next 
            else:
                # 移动end ， 直到end 位于重复的尾端
                while(True):
                    if end.next == None:
                        break 
                    if end.next.val != end.val :
                        break 
                    if end.val == end.next.val :
                        end = end.next 
                cur.next = end.next 

        return head.next


# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，
# 返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

#-*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# nums = [1,1,1,1,1,1]
# pHead = ListNode(1)
# nxt = pHead
# for i in nums[1:]:
#     node  = ListNode(i)
#     nxt.next = node 
#     nxt = node

class Solution:
    def deleteDuplication1(self, pHead):
        # 拿到节点 
        cur = pHead
        # 判断其是否和下一个元素重复

        # 不重复，开始判断他的下一个和下下个是否重复




    def deleteDuplication2(self, pHead):
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

        # 拿到下一个不重复的节点：
        # 分析当前处理的节点
        cur = head
        while(True):
            # 如果他的下一个元素不是重复元素
            while(cur.next.next == None or cur.next.next.val != cur.next.val ):
                cur = cur.next
                if cur.next == None:
                    break
            # 现在，cur要么移动到末尾，要么对应下一个元素是一个重复值
            if cur.next != None:
                # 跳过重复的结构：
                nxt = cur.next
                while(nxt.next and nxt.next.val == nxt.val):
                    nxt = nxt.next
                cur.next =nxt.next
            if cur.next == None:
                break
        return head.next
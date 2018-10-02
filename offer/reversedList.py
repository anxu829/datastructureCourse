#-*- coding:utf-8 -*-

class Solution:
    def ReverseList(self, pHead):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None
        # nums = [1,2,3,3,4]
        # pHead = ListNode(1)
        # nxt = pHead
        # for i in nums[1:]:
        #     node  = ListNode(i)
        #     nxt.next = node 
        #     nxt = node

        f = ListNode(-1)
        q = pHead
        #if q.next == None:
        #    f = q 
        while(True):
            if q == None:
                break
            else:
                r = q.next
                q.next = f.next
                f.next = q 
                q = r

        return f.next

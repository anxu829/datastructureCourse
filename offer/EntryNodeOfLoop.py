#-*- coding:utf-8 -*-

class Solution:
    def EntryNodeOfLoop(self, pHead):
        class ListNode:
            def __init__(self, x):
                self.val = x
                self.next = None
        # nums = [1,2,3,4,5,6]
        # pHead = ListNode(1)
        # nxt = pHead
        # for i in nums[1:]:
        #     node  = ListNode(i)
        #     nxt.next = node 
        #     nxt = node

        # nxt.next = pHead.next.next

        pSlow = pHead
        pFast = pHead

        status = -1
        while(True):
            if pSlow.next == None:
                break
            if pFast.next == None and pFast.next.next == None:
                break
            pSlow = pSlow.next
            pFast = pFast.next.next
            if pFast == pSlow:
                status =1
                break

        # 如果找到环
        if status == -1:
            return None

        if status ==1:
            longOfCircle = 0
            copy = pFast
            while(True):
                pFast = pFast.next
                longOfCircle +=1
                if pFast == copy:
                    break

            pFront = pHead
            pBehind = pHead

            # 把pFront 向前移动K -1 个单位
            for i in range(longOfCircle):
                pFront = pFront.next

            while(True):
                if pFront == pBehind:
                    break
                else:
                    pFront = pFront.next
                    pBehind = pBehind.next
            return pFront

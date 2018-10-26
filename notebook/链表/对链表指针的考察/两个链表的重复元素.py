# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        
        # 排除异常情况
        if pHead1 == None and pHead2 != None:
            return pHead2 
        if pHead2 == None and pHead1 != None:
            return pHead1 
        if pHead1 == None and pHead2 == None:
            return None


        # 首先需要获得每个链表的长度
        count1 = 1
        cur = pHead1
        # pHead1 = 1         -> 2       -> 
        #         cnt  = 1    cnt = 2
        while(cur!=None):
            cur = cur.next
            count1 += 1
        count2 = 1
        cur = pHead2
        while(cur!=None):
            cur = cur.next
            count2 += 1
        
        # 现在拿到两个链表的长度了
        # link1 : 1 - 2- 3  -3 -  4 - 5 - 6
        # link2 :        7 - 8 -  4 - 5 - 6
        # link1 长度为 7 ， link2 长度为 5 相差 2 ，则 需要把长的先走出去两个单位


        # 根据长短设置第一个链表为长的，第二个为短的
        if count1 >= count2:
            longest = pHead1
            shortest = pHead2

            longest_n = count1 
            shortest_n = count2
        else:
            longest = pHead2
            shortest = pHead1 
            
            longest_n = count2
            shortest_n = count2

        # 将长链表的指针首先移动 count1 - count2 个单位
        cur_long = longest
        for i in range(count1 - count2):
            cur_long = cur_long.nxt 
        cur_short = shortest
        while(cur_long != cur_short):
            cur_long = cur_long.next
            cur_short  = cur_short.next
        return cur_long
            

        

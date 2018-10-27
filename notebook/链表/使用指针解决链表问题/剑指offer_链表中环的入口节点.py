# -*- coding:utf-8 -*-

'''
环思路 ：
# 设置两个指针，一块一慢 ,start ,end 
# if start 能走， end 能走
    走至连个相遇
# 若退出循环的时候；两个节点不一致：则认为到头了，返回false
# 若位置一致，则进行下一步


# 错误：
 1 (pFast.next  !=None and pFast.next.next !=None) 
    要考虑传入的只有一个节点的情况
 2 要考虑没有环前面，只有环的情况，即考虑哪些部分是可能出现可能不出现的
 3 一块一慢的指针的问题：
    判断条件里，(pSlow.next != None and (pFast.next  !=None and pFast.next.next !=None) and  pFast != pSlow)
    有pFast != pSlow ， 但是注意到他们最开始都在头节点，即是一样的位置，会跳过while
    解决：如果可以走，就先把slow和fast走出去
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # 难点：万一没有环

        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        
        pFast = pHead.next.next
        pSlow  = pHead.next
        # pSlow 要有下一个节点
        # pFast 要有下两个节点

        while(pSlow.next != None and (pFast.next  !=None and pFast.next.next !=None) and  pFast != pSlow):
            pFast = pFast.next.next
            pSlow = pSlow.next
        # 这时候需要判断是否是两者相同
        if pFast != pSlow:
            return None
        # 现在我们知道是一个闭环了
        # 1  -  2 - 3 -4- 1
        # cur   pSlow 
        count = 1
        cur = pSlow
        pSlow = cur.next
        while(pSlow != cur):
            pSlow = pSlow.next
            count +=1
        # 此时count 应该就是环的长度
        # 1 - 2 -3 - 4 - 5
        #     |          |   
        #     ------------
        # 
        # 从首结点开始移动4格
        start1 = pHead
        for i in range(count):
            start1 = start1.next
        start2 = pHead
        # 让这两个同时走
        while(start1 != start2):
            start1 = start1.next
            start2 = start2.next
        return start1 
        

if __name__ == '__main__':
    # 测试用例1 
    
    # pHead = ListNode(1)
    # pHead.next = pHead
    # res = Solution().EntryNodeOfLoop(pHead)


    # 测试用例2 
    # 1 - 2 - 3 - 4 -5
    #         |      |
    #          ------
    nums = [1,2,3,4,5]
    pHead = ListNode(-1)
    nxt = pHead
    for i in nums:
        node  = ListNode(i)
        nxt.next = node 
        nxt = node
    nxt.next = pHead.next.next.next
    res = Solution().EntryNodeOfLoop(pHead.next)
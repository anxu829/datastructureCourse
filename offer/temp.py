# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        pass
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
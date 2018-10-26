# -*- coding:utf-8 -*-

# 依旧是首先考虑简单的情形
# 然后考虑使用如下思路
# 使用节点reverse 记录反转链表
# 使用 cur 记录当前，用nxt 记录下一个节点，然后cur 接到reverse（cur.next = reverse , reverse = cur）

# 常见错误
# [注意]这里有一个小技巧，reverse 必须直接接在第一个上，而cur从第二个开始遍历
# [注意] 不要把 cur.next  写成 cur.nxt ，写东西思路必须清晰
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # 首先排除异常情况
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        if pHead.next !=None and pHead.next.next == None:
            cur = pHead
            nxt = pHead.next
            nxt.next = cur
            nxt.next.next = None
            return nxt 
        # 现在节点至少会有三个以上
        reverse = pHead
        cur = pHead.next
        nxt = cur.next
        # 把反转链表的末尾置为空节点
        reverse.next = None 
        while(nxt != None):
            # 把cur的下一个节点连接到 reverse
            cur.next = reverse
            reverse = cur
            # nxt 中保留了剩余的节点的信息
            cur = nxt 
            nxt = cur.next
        # 现在，cur应该是最后一个节点
        cur.next = reverse
        reverse  = cur 
        return reverse





        



if __name__ == '__main__':
    


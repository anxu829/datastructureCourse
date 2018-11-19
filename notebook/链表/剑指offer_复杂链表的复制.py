# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None



# [注意] 复制步骤必须 创建一个节点

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead == None:
            return pHead
        # 如果只有一个节点：
        if pHead.next == None:
            #[错误] 记得复制一下
            temp =  RandomListNode(pHead.label)
            temp.next = None
            return temp 
        # 复制复杂链表：
        # 相当于要一边遍历链表，一遍在链表的下一个位置加入新的节点
        # 首先指向这个链表的第一个节点，然后cur会逐步遍历链表的每一个节点
        cur = pHead
        # A - B - None
        while(cur !=None):
            # 当cur的下一个不是None，即cur不是最后一个节点
            # 新建一个节点,复制其值
            tempNode = RandomListNode(cur.label)
            # 把节点插入到 cur 和 cur的下一个之间
            tempNode.next = cur.next
            cur.next = tempNode
            # 把cur置换为下一个节点
            # 【】 - 【】 - None
            cur = tempNode.next
        # 完成随机链接的复制，
        # A - A - B - B - None
        # |       |   
        # ---------
        # 【难点】需要跳步的访问数据
        cur = pHead
        # 当cur 非原始链表的最后一个节点
        while(cur !=None):
            # 这里要考虑cur.random 可能是None的情形
            if cur.random != None:
                cur.next.random = cur.random.next
            # 将游标移动到原始链表的下一个节点
            cur = cur.next.next
        # 现在cur 在最后一个节点上
        # 完成复杂链表的分离：
        # A - A - B - B - None
        # |       |   
        # ---------
        cur = pHead
        # 构建新的链表：记录其开始节点
        new = pHead.next 
        # cur_new为随着遍历的过程，新链表的当前游标位置
        cur_new = new
        while(cur != None):
            cur.next = cur.next.next 
            if cur.next != None:
                cur_new.next = cur.next.next 
            else:
                cur_new.next = None
            cur = cur.next 
            # 【错误】 注意到cur 更新后可能是None
            if cur != None:
                cur_new = cur.next 
        return new 


if __name__ == '__main__':
    a = RandomListNode('a')
    a.next = RandomListNode('b')
    a.random = a.next
    s = Solution().Clone(a)




        






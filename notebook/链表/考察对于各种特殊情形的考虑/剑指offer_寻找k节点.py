# -*- coding:utf-8 -*-

#输入一个链表，输出该链表中倒数第k个结点。


'''
核心思路：
先找到链表的正数第k个

# 问题：链表不一定有k个节点
# 所以如何解决：
    首先找第k个，这个过程中，如果没有k 个，就结束，return false
# 问题2 ： 如果k 非正数 ， 
# 问题3 ：如果链表非空

# 举例子：
{1，2，3，4，5，6}
{倒数第3个的话，第二个指针必须移动到3，即第三个节点}}

# 方法2 ， 构造一个定长的queue ，只保存足够长度的信息
{1 , 2 , 3 , 4 , 5 , 6 }

倒数第四个的话，
只需要存储 {3,4,5,6}
所以是需要存储 {n - k }的长度的数组

# 方法
import Queue
myqueue = Queue.Queue(maxsize = 10)

'''
import Queue

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # 首先判断k的合法性
        if k <= 0:
            return None
        # 判断head的合法性
        if head == None:
            return head
        
        # 寻找正着数的第k个节点
        count = 1
        cur = head
        # 若有下一个节点，则前进一步
        # 如 {1，2}，k = 1  -> k =2  
        while (cur.next != None and count != k  ):
            cur = cur.next
            count +=1
        if count != k:
            # 说明现在没有走到合理的位置
            return None
        else:
            start = head
            while(cur.next != None):
                cur = cur.next
                start = start.next
            return start 
        
        
if __name__ == '__main__':
    nums = [1,2,3,4,5]
    pHead = ListNode(1)
    nxt = pHead
    for i in nums[1:]:
        node  = ListNode(i)
        nxt.next = node 
        nxt = node
    res = Solution().FindKthToTail(pHead.next,6)
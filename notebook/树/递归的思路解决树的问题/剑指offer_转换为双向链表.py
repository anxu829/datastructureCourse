# -*- coding:utf-8 -*-

# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。

#【错误】要考虑到最后的返回必须具有全局的最左和最右


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Convert(self, pRootOfTree):
        f,s = self.recursive(pRootOfTree)
        return f 
    def recursive(self,pRootOfTree):
        # 首先判断是否是一个空链表
        if pRootOfTree == None:
            rear = front = None
            return rear,front 
        # 现在不是一个空链表，判断是否有子节点
        if pRootOfTree.left == None and pRootOfTree.right ==None:
            rear = front = pRootOfTree
            return rear , front
        # 初始时，左右都默认为这个节点本身
        totalLeft =  totalRight = pRootOfTree
        # 现在两边不可能都空节点
        if pRootOfTree.left != None :
            rear , front = self.recursive(pRootOfTree.left)
            front.right = pRootOfTree
            pRootOfTree.left = front 
            # 拿到全局的最左侧
            totalLeft = rear 
        if pRootOfTree.right != None:
            rear , front = self.recursive(pRootOfTree.right)
            rear.left = pRootOfTree
            pRootOfTree.right  = rear
            totalRight = front
        return totalLeft ,  totalRight

if __name__ == '__main__':
    seq = [10,6,14,4,8,12,16]
    nodelist = [TreeNode(val) for val in seq]
    head = nodelist[0]
    head.left = nodelist[1]
    head.right = nodelist[2]
    head.left.left = nodelist[3]
    head.left.right = nodelist[4]
    head.right.left = nodelist[5]
    head.right.right = nodelist[6]
    f,s = Solution().Convert(head)
    head = 0


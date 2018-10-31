# -*- coding:utf-8 -*-

#请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
#问题的核心： 对称结构是递归定义的：
#对称 -> 对应的左节点和右节点的值是一样的，且节点的子树满足对称关系（这是一个递归定义的过程 ）

# 技巧：从 if pRoot1 == None and pRoot2 == None: 到 pRoot1 == None or pRoot2 == None:


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetricalBiTree(self,pRoot1 , pRoot2):
        # 首先解决 None的问题，避免无法访问
        if pRoot1 == None and pRoot2 == None:
            # 完成匹配，认为成功
            return True 
        # 如果一边已经到头，另一边没有到头，则认为匹配失败
        if pRoot1 == None or pRoot2 == None:
            return False
        # 现在两个子树都有值
        if pRoot1.val == pRoot2.val:
            return self.isSymmetricalBiTree(pRoot1.left,pRoot2.right) and  self.isSymmetricalBiTree(pRoot1.right,pRoot2.left)
        else:
            return False


    def isSymmetrical(self, pRoot):
        if pRoot == None:
            return True
        if pRoot.left == pRoot.right and pRoot.left ==  None:
            return True
        else:
            return self.isSymmetricalBiTree(pRoot.left,pRoot.right)
    
        
if __name__ == '__main__':
    T = TreeNode(8)
    T_l = TreeNode(6)
    T_r = TreeNode(6)
    T_ll = TreeNode(5)
    T_rr = TreeNode(5)
    T_lr = TreeNode(7)
    T_rl = TreeNode(7)
    T.left = T_l ; T.right = T_r
    T_l.left = T_ll ; T_l.right = T_lr
    T_r.left = T_rl ; T_r.right = T_rr 
    Solution().isSymmetrical(T)
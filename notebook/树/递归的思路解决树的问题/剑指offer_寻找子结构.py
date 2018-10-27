# -*- coding:utf-8 -*-

# 【常犯错误】 树的题目，一定要考虑节点的val和next能否访问的问题，即需要判断即将访问的节点是否为空
# 本题目难点：
# 子结构 和 目标结构匹配/不匹配有几种可能：
#  1 目标结构已经为空，但是子结构依旧不问空，即目标结构已经遍历到叶子节点，返回True
#  2 目标结构不为空，但是子结构已经为空，这是【最容易忽略的】
#  3 目标结构和子结构在根节点位置的val 不一样，返回false
#   
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def hasSameStruct(self,pRoot1,pRoot2):
        # 如果走完，表示已经成功地匹配了所有的root2节点
        if pRoot2 == None:
            return True 

        if pRoot1 == None and pRoot2 != None:
            return False
        else:
            # 如果在这个节点的位置发生了匹配
            if pRoot1.val == pRoot2.val:
                # 对左子树和右子树进行匹配
                return self.hasSameStruct(pRoot1.left,pRoot2.left) and self.hasSameStruct(pRoot1.right , pRoot2.right)
            else:
                return False                
                
    def HasSubtree(self, pRoot1, pRoot2):
        # 首先避免待匹配结构为空
        if pRoot2 == None:
            return False
        # 现在待匹配结构不为空
        # 递归的完成匹配 ：
        if pRoot1 == None:
            # 表示走到底了还没有进行匹配
            return False
        # 现在是还没有走到底的情形
        if pRoot1.val == pRoot2.val:
            # 表示在这一个地方可能发生匹配
            if self.hasSameStruct(pRoot1,pRoot2):
                # 表示他们真的匹配了
                return True 
            else:
                # 说明没有匹配
                return self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2) 
         
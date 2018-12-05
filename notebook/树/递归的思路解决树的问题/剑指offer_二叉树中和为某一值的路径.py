# -*- coding:utf-8 -*-
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。(注意: 在返回值的list中，数组长度大的数组靠前)

#【错误】 
"""
# self._findPath(root.left ,target - root.val , current , res  )
# 递归需要考虑 root.val 是否为空
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    
    def _findPath(self,root , target , current , res ):
        
        if root.left == root.right == None :
            # 到达根节点
            if root.val == target:
                current.append(root.val)
                res.append(current[:])
                current.pop()
        else:
            current.append(root.val)
            if root.left != None:
                self._findPath(root.left ,target - root.val , current , res  )
            if root.right !=None:
                self._findPath(root.right,target - root.val , current , res  )
            current.pop()
    def FindPath(self, root, expectNumber ):
        if root == None:
            return []
        # need 3 elements
        # target  : 当前需要处理的变量
        # res     : 记忆所有处理完的结果的list
        # current ：处理到当前时刻，希望加入到res 中的 list的当前状态

        # step1 : 定义所有东西的初始值
        target  = expectNumber
        res     = []
        current = [] 
        self._findPath(root,expectNumber,current,res)
        return res 

    def findPath2(self,node,val , currentLis , res ,expectNumber):
        # 返回二维列表，内部每个列表表示找到的路径
        # 要将结果更新到currentLis中
        # 判断是或可以返回
        
        # 如果访问到None 仍然没有搞定，return，但是不做任何事情
        if node == None:
            return 
        if node.val + val < expectNumber:
            # 现在还没有搞定
            currentLis.append(node.val)
            self.findPath(node.left , val  + node.val , currentLis ,res  ,  expectNumber )
            self.findPath(node.right , val  + node.val , currentLis ,  res , expectNumber )
            currentLis.pop()
        if node.val + val == expectNumber:
            # 判断是否是叶子节点
            if node.left == node.right == None:
                currentLis.append(node.val)
                res.append(currentLis[:])
                currentLis.pop()
            return
        if node.val + val > expectNumber:
            return
    def FindPath2(self, root, expectNumber ):
        
        # 首先建立一个记忆用的节点
        currentLis = []
        # 初始化当前求和结果
        val = 0
        # 从root节点开始
        node = root 
        # 设置存储最终结果的res
        res  = []
        # 本类型题目：一定要传入res 的 lis，在递归中进行修改
        self.findPath(node,val,currentLis , res , expectNumber )
        return res 
if __name__ == "__main__":
    # N = TreeNode(10)
    # N_L = TreeNode(5)
    # N_R = TreeNode(12)
    # N_L_l = TreeNode(4)
    # N_L_r = TreeNode(7)
    # N.left = N_L ; N.right = N_R
    # N_L.right = N_L_r
    # N_L.left = N_L_l
    
    N = TreeNode(5)
    N_l = TreeNode(4)
    N_ll = TreeNode(3)
    N_lll = TreeNode(2)
    N_llll = TreeNode(1)
    N.left = N_l
    N_l.left = N_ll
    N_ll.left = N_lll
    N_lll.left = N_llll
    Solution().FindPath(N,22)
    print('hi')


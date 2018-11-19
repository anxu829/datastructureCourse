# -*- coding:utf-8 -*-

# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

# 我的解决思路：必须维护两个lis ， cur 维护正在遍历的层 ，nxt 维护的是cur的下一层
# 按照层深度的奇偶性，插入的时候 进行reverse

# 【注意】：解决过程中一定要记得把相应的flag的值进行相应的变化

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot == None:
            return []
        else:
            # 至少头节点有值
            if pRoot.left == pRoot.right == None:
                return [[pRoot.val]]
            else:
                # 现在至少有两层的信息
                res = []
                deep = 1
                cur = [pRoot]
                while(cur != []):
                    # 构造nxt
                    nxt = []
                    for node in cur:
                        if node.left != None:
                            nxt.append(node.left)
                        if node.right !=None:
                            nxt.append(node.right)
                    # 把cur的值放入res
                    if deep % 2 == 1:
                        res.append([n.val for n in cur])
                    else:
                        res.append(list(reversed([n.val for n in cur])))
                    cur = nxt 
                    deep = deep + 1
                return res
        

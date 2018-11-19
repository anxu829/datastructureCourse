# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

# [4,8,6,12,16,14,10]

# 错误：对于[1,2,3]是合理的

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None:
            return False
        # 判断递归的终止状态
        if len(sequence) == 1:
            # 只有一个节点：
            return True
        if len(sequence) == 2:
            return True
        if len(sequence) == 3:
            return True
            # a,b,c = sequence      
            # if b>= c and c >= a:
            #     return True
            # else:
            #     return False
        # 现在sequence 一定是大于三个的
        # 首先拿到最后的一个节点
        headNode = sequence[-1]

        # 从前往后，找到第一个大于等于headNode 的节点
        loc = 0
        while(sequence[loc] < headNode):
            loc +=1
        # 现在loc的位置：
        # 如果位于首节点：说明没有左子树
        # 如果位于最后一个节点，说明没有右子树
        # 如果位于中间，说明有左子树也有右子树，loc位于右子树的第一个位置
        if loc == 0:
            # 说明全部是右子树 , 检查右子树是否是有小于头节点的元素
            if min(sequence[loc:-1] ) >= headNode:
                # 说明是合理的,继续判断右子树的合理性
                return self.VerifySquenceOfBST(sequence[:-1])
            else:
                return False
        if loc == len(sequence) - 1:
            if max(sequence[:-1]) <= headNode:
                return self.VerifySquenceOfBST(sequence[:-1])
            else:
                return False
        else:
            # 分段检查合理性：
            if max(sequence[:loc]) <= headNode and min(sequence[loc:-1]) >= headNode:
                return self.VerifySquenceOfBST(sequence[:loc]) and self.VerifySquenceOfBST(sequence[loc:-1])
            else:
                return False
Solution().VerifySquenceOfBST([1,2,3,4,5])
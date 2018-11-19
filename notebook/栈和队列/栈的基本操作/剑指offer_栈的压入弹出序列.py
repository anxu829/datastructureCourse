# -*- coding:utf-8 -*-

#输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
# 假设压入栈的所有数字均不相等。
# 例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
# 但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）

# 要多考虑只有一个元素的情形，因为最后的退出条件是：idx == len(popV) -1

'''
解题思路：维护一个实际的栈

'''

class Solution:
    def IsPopOrder(self, pushV, popV):
       # 首先判断两个lis 是否为 空
        if pushV == popV == None :
           return True
        elif len(pushV) == len(popV) == 1:
            if popV[0] == pushV[0]:
                return True
            else:
                return False
        else:
            idxForPushV = 0
            # 建立一个空栈
            stack = []
            for idx, v in enumerate(popV):
                # 如果 popV 的元素和栈顶的不一样 且pushV中还有变量：则从pushV中入栈
                while (stack == [] or v != stack[-1] ) and idxForPushV < len(pushV):
                    stack.append( pushV[idxForPushV] )
                    idxForPushV += 1
                # 现在可能的情况：
                # 和栈顶的元素一样
                # 和栈顶的元素不一样，但是pushV中没有元素可以提取了

                # 如果和栈顶元素一致：进行pop
                if v == stack[-1]:
                    stack.pop()
                else:
                    break
            if idx == len(popV) -1:
                return True
            else:
                return False
if __name__ == '__main__':
    lis1 = [1]
    lis2 = [2]
    res = Solution().IsPopOrder(lis1,lis2)
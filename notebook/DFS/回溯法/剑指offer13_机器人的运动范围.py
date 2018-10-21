#-*-coding:utf-8-*-
"""
题目的难点：
1 关于mask的使用
    这道题的mask是不还原的
2 算法的流程：
    对每一个节点：
        1 回溯的目的：返回从这个节点开始能够遍历的元素位置
        2 输入：
            1 行列情况
            2 当前走到的位置
            3 mask ： 是还未遍历这个节点的状态
        3 输出：一个能遍历路径的visted 矩阵
            【1】包含对这个节点自身的判断？
            【2】他往下的元素的判断？
        
        4 算法主体：
            4.1 判断其能不能走
            4.2 判断其周围能不能走，若能走，返回下一个点的走下去的情况
        
        5 写的时候犯的错误
            5.1
                sum([int(i) for i in str(i+1)+str(j+1)])
                这一步会覆盖循环主体的变量 i 
            5.2 未设立递归终止条件，递归死循环
                回溯一定要 设置判断下一步是否还需要走 ： mask[i-1][j] != 1
"""
rows  = 10
cols  = 10
threshold = 5
# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        mask = [[0]*cols for i in range(rows)]
        def counter(rows,cols,thres,i,j,mask):
            # 判断是否能往下走
            if sum([int(v) for v in str(i)+str(j)]) > thres:
                return 0
            else:
                # else 说明此矩阵可以走
                mask[i][j] = 1 
                print(i,j , sum([int(v) for v in str(i)+str(j)]))
                # 向上走：
                if i !=0 and mask[i-1][j] != 1:
                    counter(rows,cols,thres,i-1,j,mask)
                # 向下走:
                if i != rows - 1 and mask[i+1][j] != 1:
                    counter(rows,cols,thres,i+1,j,mask) 
                # 向左走
                if j != 0 and mask[i][j-1] != 1:
                    counter(rows,cols,thres,i,j -1 ,mask) 
                # 向右走
                if j != cols - 1 and mask[i][j +1] != 1:
                    counter(rows,cols,thres,i,j+  1 , mask) 
                return 0
                        
        counter(rows,cols,threshold,0,0,mask)
        return sum([sum(i) for i in mask])

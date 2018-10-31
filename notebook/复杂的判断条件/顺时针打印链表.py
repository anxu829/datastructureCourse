# -*- coding:utf-8 -*-


# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
# 例如，如果输入如下4 X 4矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 
# 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


# 【错误】忘记加入对 rowE ， colE ， rowS ， colS 的状态更新
# 【错误】 通不过 [[1],[2],[3],[4],[5]]

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        rowE = len(matrix) - 1 
        colE = len(matrix[0]) - 1
        rowS = 0
        colS = 0
        while(colS <= colE and  rowS <= rowE):
            # 首先总是可以打印第一行的
            for  col in range(colS,colE+1):
                res.append(matrix[rowS][col])
            # 然后判断是否走第二段：
            if rowE - rowS >=2 :
                for row in range(rowS+1,rowE):
                    res.append(matrix[row][colE])
            # 判断是否要走第三段
            if rowE != rowS:
                for col in reversed(range(colS,colE+1)):
                    res.append(matrix[rowE][col])
            # 判断是否要走第四段：
            if rowE - rowS >=2  and colE != colS:
                for row in reversed(range(rowS+1,rowE)):
                    res.append(matrix[row][colS])

            # 更新状态
            rowS = rowS + 1 ; colS = colS + 1 ; rowE = rowE -1 ; colE = colE - 1;
        return res
if __name__ == '__main__':
    matrix = [[1],[2],[3],[4],[5]]
    res = Solution().printMatrix(matrix)
    print(res)




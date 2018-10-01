matrix = [
['a' , 'b' , 't' , 'g'],
['c' , 'f' , 'c' , 's'],
['j' , 'd' , 'e' , 'h']
]

target = 'bfce'
rowNum = len(matrix)
colNum = len(matrix[0])

# create a mask to save status

mask = [ [ 0 for j in range(colNum) ]  for i in range(rowNum)]

start = target[0]


def dfs(matrix,mask , row , col , target , searchTarget ):
    global rowNum,colNum
    
    if searchTarget  == len(target) -1 :
        return True
    else:
        # 首先，把该位置标记为1
        mask[row][col] = 1 
        # 随后，get下一个字符串
        nextTarget = target[searchTarget+1]
        # 向下搜索下一个位置
        # 上;
        flag = -1
        if row != 0:
            if matrix[row-1][col ] == nextTarget and mask[row-1][col] == 0 :
                if dfs(matrix,mask,row-1,col,target,searchTarget +1):
                    return True
                    flag = 0
        # 下
        if row != rowNum:
            if matrix[row+1][col ] == nextTarget and mask[row+1][col] == 0 :
                if  dfs(matrix,mask,row+1,col,target,searchTarget +1):
                    return True
                    flag = 0
        # 左 
        if col != 0:
            if matrix[row][col -  1 ] == nextTarget and mask[row][col -1 ] == 0:
                if  dfs(matrix,mask,row ,col -1 ,target,searchTarget +1):
                    return True
                    flag = 0
        # 右
        if col != colNum :
            if matrix[row][col +  1 ] == nextTarget and mask[row][col + 1 ] == 0:
                if dfs(matrix,mask,row ,col + 1 ,target,searchTarget +1):
                    return True 
                    flag = 0
        mask[row][col] = 0 
        if flag == -1 :
            return False 
            





for row  in range(rowNum):
    for col  in range(colNum):
        # 寻找递归开始位置
        if matrix[row][col] == start:
            status =  dfs(matrix,mask,row,col, target , 0 )
            if status == True:
                break 
        

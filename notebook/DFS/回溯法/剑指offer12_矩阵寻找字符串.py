lis = [['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
target = 'bfce'
mask = [ [0] * len(lis[1]) for i in range(len(lis))]
flag = 0

def dfs(target,lis,mask,i,j):
    # 这个逻辑下，传入的部分一定是满足使得 这个位置的元素和 待探索的字符串的元素相同的
    # 先遮挡住这个位置
    mask[i][j] = 1
    
    if target[1:] == '':
        return 1
    
    state = 0
    # 朝上走
    if i != 0 and target[1] == lis[i-1][j]  and mask[i-1][j] == 0:
        state = dfs(target[1:],lis,mask,i-1,j)

    # 朝下走
    if i != len(lis) -1 and target[1] == lis[i+1][j] and mask[i+1][j] == 0:
        state =  dfs(target[1:],lis,mask,i+1,j)

    # 朝左走
    if j != 0 and target[1] == lis[i][j-1] and mask[i][j-1] == 0 :
        state =  dfs(target[1:],lis,mask,i,j-1)

    # 朝右走
    if j != len(lis[1]) -1 and target[1] == lis[i][j+1] and mask[i][j+1] == 0:
        state =  dfs(target[1:],lis,mask,i,j+1)
    
    mask[i][j] = 0
    

    if state == 0:
        return 0
    else:
        return 1


for i in range(len(lis)):
    for j in range(len(lis[0])):
        char = lis[i][j]
        if char ==target[0]:
            flag = dfs(target,lis,mask,i,j)
        
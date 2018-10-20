lis = [50 , 10 , 90 , 30  , 70 , 40 , 80,60,20 ]
def buildToEnd(lis,end):
    def changeNode(lis,node , end ):
        l = 2*(node + 1)  -1
        r = 2*(node + 1)  +1 -1
        if l < end and r < end:
            change =  l if lis[l] > lis[r] else  r
            if lis[node] < lis[change] :
                temp = lis[node]
                lis[node] = lis[change]
                lis[change] = temp
                changeNode(lis,change , end)
        # 只有左节点：
        if l < end and  r >= end:
            if lis[node] < lis[l]:
                temp = lis[node]
                lis[node] = lis[l]
                lis[l] = temp
                changeNode(lis,l,end)
    lastNode = int(end /2)
    for node in range(lastNode,-1,-1):
        changeNode(lis,node,end)
        

# lis =[10, 20, 30, 40, 50, 60, 70, 80, 90]
# buildToEnd(lis,2)


for idx in range(len(lis),0,-1):
    print(lis,idx)
    buildToEnd(lis,idx)
    temp = lis[0]
    lis[0] = lis[idx - 1]
    lis[idx -1] = temp 


    
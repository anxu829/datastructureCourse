lis = [4 ,1 , 7 , 6 , 9 ,2 , 8 , 0 , 3 , 5]
K = 3
def quikSort(lis,start , end):
    left  = start  
    right = end 
    while (left < right):
        while( left < right and lis[right] >= lis[start] ):
            right -=1
        while( left < right and lis[left] <= lis[start]):
            left +=1
        temp = lis[left]
        lis[left] = lis[right]
        lis[right] = temp
    temp = lis[start]
    lis[start] = lis[left]
    lis[left] = temp
    print(lis)
    return left




start  = 0
end = len(lis) - 1
while(start < end):
    left = quikSort(lis, start, end )
    if len(lis) - left > K :
        start = left + 1
    elif len(lis) - left < K:
        end = left - 1
    else:
        print("get you !",lis[left])


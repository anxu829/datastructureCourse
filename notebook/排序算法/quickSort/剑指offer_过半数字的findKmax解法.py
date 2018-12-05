

# 【quikSort】 的要点：
# 1.1 left 和 right 都是顶着格子开始的
# 所以在left的判断中：
#
#        while(left < right and lis[left] <= lis[head] ):
#            left += 1
# 要注意一定是  lis[left] <= lis[head]  而不能是 lis[left] <= lis[head]
# 1.2 start , end 直接对应到原始数据上的位置，所以head返回的直接是原始数据的某个位置


# -*- coding:utf-8 -*-
def quickSort(lis,start,end):
    # 对lis的start 到end进行排序，并返回start最后的位置
    head = start # 获取这一轮排序的标志物

    # 这里的一个特点是left 和 right 的初始取值是顶着的
    # 注意 ， start ，end 直接对应坐标，不要呗python的风格影响判断
    left  = head     
    right = end 

    # 然后开始走动
    while(left < right):
        # 必须先走right，且right包含的范围是大于lis[head]
        while(left < right and lis[right] > lis[head] ):
            right -= 1
        while(left < right and lis[left] <= lis[head] ):
            left += 1
        # break 的条件，right 要么等于left ， 要么比head 小
        # 完成left 和 right 位置上的交换
        lis[left] , lis[right] = lis[right]  , lis[left]    
    # 完成交换
    temp = lis[head]
    lis[head] = lis[right]
    lis[right] = temp 
    return right


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        
        lis = numbers
        start = 0 
        end = len(lis) - 1
        M = len(lis ) // 2
        while(True):
            k = quickSort(lis,start,end)    
            if k > M:
                end = k- 1
            elif k<M:
                start = k+ 1
            else:
                break 
        
        from collections import Counter
        if Counter(lis)[lis[k]] >= len(lis) // 2 + 1 :
            return lis[k]
        else:
            return 0
if __name__ == "__main__":
    lis = [1,2,3,2,4,2,5,2,3]
    k = Solution().MoreThanHalfNum_Solution(lis)
    print(k)
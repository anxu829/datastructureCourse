# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


# 错误：
## end 初始值是 -1 而不是 array[-1] , 需要时刻记住自己是在访问数组的值还是访问下标
## 在算法题中，避免使用 -1 这种索引，会导致 如 start < end 这种判断条件不能使用
## 注意，在剑指offer当中，是不要求保证顺序不变的
'''


class Solution:
    def reOrderArray(self, array):
        # 首先设立两个游标
        start = 0
        end = len(array) - 1
        # 考虑特殊情形：
        if len(array) < 1:
            return True 
        while(start < end ):
            # start 寻找偶数
            while(start < end and array[start] % 2 == 1):
                start +=1
            # end 寻找奇数
            while(start < end and array[end] %2 == 0):
                end -= 1
            array[start] ,array[end] = array[end] , array[start]
    
if __name__ == '__main__':
    array =[1,2,3,4,5,6,7]
    Solution().reOrderArray(array)
    print(array)

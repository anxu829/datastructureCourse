# -*- coding:utf-8 -*-
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


# 错误：
## end 初始值是 -1 而不是 array[-1] , 需要时刻记住自己是在访问数组的值还是访问下标
## 在算法题中，避免使用 -1 这种索引，会导致 如 start < end 这种判断条件不能使用
## 下面介绍牛客网的问题的解法
'''


class Solution:    
    def reOrderArray(self, array):
        pass 
    def reOrderArray1(self, array):
        # write code here
        odd,even=[],[]
        for i in array:
            odd.append(i) if i%2==1 else even.append(i)
        return odd+even
    def reOrderArray2(self, array):
        # 都是简单的问题
        return sorted(array,key=lambda c:c%2,reverse=True)
if __name__ == '__main__':
    array =[1,2,3,4,5,6,7]
    Solution().reOrderArray(array)
    print(array)
#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
# 思路：首先需要判断 exponent 是否是一个大于零的数字


# 解决过程中遇到的问题：
# 在类内部调用函数需要使用 self.Power的形式
# if else 的条件不能有重叠


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if  exponent >0:
            if exponent == 1:
                return base 
            if exponent == 2:
                return base ** 2
            if exponent %2 ==0:
                power = self.Power(base,exponent/2) 
                return power * power 
            else:
                power = self.Power(base,int(exponent/2))
                return power * power * base 
        elif exponent == 0:
            return 1
        else:
            return 1/ self.Power(base,abs(exponent))
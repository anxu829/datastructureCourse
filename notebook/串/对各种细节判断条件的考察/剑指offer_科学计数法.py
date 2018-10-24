# -*- coding:utf-8 -*-
'''
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。


# 错误：可能有12e这种例子，即出现 . 直接出现e 
# 错误：注意到没遇到 . 也可能构成合法数字，即要想明白有哪些合法数字
# loc!=len(s) and s[loc] >= '0' and s[loc] <= '9'   , loc != len(s) 要放在前面
# s[loc] 写成了 loc
# 最前面的正负号只能有一个

'''
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        # 首先确认第一个位置不是正负号
        if s == '':
            return False
        loc = 0
        if s[0] == '+' or s[0] == '-' :
            loc +=1
        
        # 一直走，直到遇到非数字的部分
        while(loc!=len(s) and s[loc] >= '0' and s[loc] <= '9'  ):
            loc = loc + 1
        if loc == len(s):
            return True
        # 现在：可能碰到 . 和 e
        if s[loc] == '.':
            if loc+1 == len(s):
                return True
            else:
                loc = loc +1
                # 一直走到下一个非数字节点
                while(loc!=len(s) and s[loc] >= '0' and s[loc] <= '9'  ):
                    loc = loc + 1
        # 若走完：则成功
        if loc == len(s):
            return True
        # 若没走完,则继续：
        if s[loc] == 'e' or s[loc] == 'E':
            if loc +1 == len(s):
                return False
            if s[loc +1] == '-' or s[loc +1] == '+':
                loc = loc +2
            else:
                loc = loc +1 
            while(loc!=len(s) and s[loc] >= '0' and s[loc] <= '9'  ):
                loc = loc + 1
            if loc == len(s):
                return True
            else :
                return False
        else:
            return False



s = '123.45e+6'
res = Solution().isNumeric(s)
        
# -*- coding:utf-8 -*-
# 难点： 不带返回的递归如何合理的进行
# 细节： 下面的return 不能写在for循环中，否则会导致后续的for循环不进行
# 难点2：回溯法，一定要记得在修改变量以进行下一步操作后，将变量还原回来，否则会出事
# 错误3 ： forPrint + str(i) 写成了  str(i) + forPrint 
        

def recursive(K,forPrint):
    if len(forPrint) == K:
        print(forPrint)
        return 'success'
    for  i in range(10):
        # 更新forPrint
        forPrint_next = forPrint + str(i) 
        print(forPrint_next)
        # 并在下一轮进行
        recursive(K,forPrint_next)
    return 'success'
 
k = 3
recursive(k,'')
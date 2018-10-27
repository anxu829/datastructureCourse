# -*- coding:utf-8 -*-
"""
常见错误：
1 这个问题不能使用循环来做，涉及到很多的递归和组合
2 注意 若 s = ‘a’ 则 s[1:]是可以使用的

"""
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # 这道题的核心：是要各种分情况讨论：
        ## 首先分析 s 不为空的情况
        if s != '':
            if pattern == '':
                return False
            # 若不存在 * 的状况：
            if len(pattern) == 1 or (pattern[1] != '*'):
                if pattern[0] == s[0]  or pattern[0] == '.':
                    return self.match(s[1:],pattern[1:])
                else:
                    return False
            # 若存在 * 的情况：
            if pattern[1] == '*':
                if pattern[0] == '.' or pattern[0] == s[0]:
                    # 是 .* 的情况
                    return self.match(s,pattern[2:]) or self.match(s[1:],pattern) or self.match(s[1:],pattern[2:]) 
                else:
                    return self.match(s,pattern[2:])
        else :
            if pattern == '':
                return True 
            # 若不存在 * 的状况：
            if len(pattern) == 1 or (pattern[1] != '*'):
                return False
                        # 若存在 * 的情况：
            if pattern[1] == '*':
                return self.match(s,pattern[2:])
            



if __name__ == '__main__':
    s = 'a'
    pattern = '.'
    result = Solution().match(s,pattern)
# -*- coding:utf-8 -*-
import copy
from  collections import Counter
class Solution:
    def permute(self,ss):
        if len(ss) == 1:
            return ss 
        # 首先取出各种元素
        res = []
        for  i in range(len(ss)):
            start = ss[i]
            ss_cp = copy.deepcopy(ss)
            ss_cp.pop(i)
            ans = self.permute(ss_cp)
            res +=  [start + i for i in ans]
        return res 
    def Permutation(self, ss):
        if ss == "":
            return []
        if len(ss) == 1:
            return [ss]
        ss_list = list(ss)
        
        ans = self.permute(ss_list)
        ans = Counter(ans).keys()
        ans = sorted(ans)
        return ans

if __name__ == "__main__":
    res = Solution().Permutation('aab')
    print(res)


        
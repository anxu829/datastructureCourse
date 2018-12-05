# -*- coding:utf-8 -*-

#【易错点:localSum 不能从0开始，因为和有可能最大都是-1】
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        localSum = -999
        localMax = [array[0]]
        
        for idx, val in enumerate(array[1:]):
            if localMax[-1] > 0:
                localMax.append(val + localMax[-1])

            else:
                localMax.append(val)
            localSum = localSum if localSum > localMax[-1] else localMax[-1]
        return localSum

if __name__ == "__main__":
    lis = [1,-2,3,10,-4,7,2,-5]
    Solution().FindGreatestSumOfSubArray(lis)
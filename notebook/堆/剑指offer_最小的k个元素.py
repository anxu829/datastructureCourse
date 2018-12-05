# 输入n个整数，找出其中最小的K个数。
# 例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。


# -*- coding:utf-8 -*-

#【特别注意，这里是要维护最大堆！！！，很容易混淆】
#【错误2】 注意，python中最麻烦的是heap.heap存放的是负值
#【错误3】 # 必须保持定长的序列 heap.heap = heap.heap[-k:]
#【考虑 k 如果大于数组的长度，返回空】
#【考虑k 如果非法 <=0 , 返回 []】
# 建立一个最大堆
import heapq
class maxHeap():
    def __init__(self):
        self.heap = []
    @classmethod
    def list_init(cls,heaplist):
        temp = cls()
        temp.heap = heaplist
        temp.heap = [ -1 * i for i in temp.heap]
        # heapify 是对于传入的参数的直接处理
        heapq.heapify(temp.heap)
        return temp
        
    def push(self,elm):
        heapq.heappush(self.heap,-elm)
    
    def pop(self):
        if len(self.heap) != 0:
            return -1 * heapq.heappop(self.heap)
        else:
            return -999

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k<= 0  or  k > len(tinput):
            return []

        heap = maxHeap()
        #开始把数据依次的push进去
        for val in tinput:
            if len(heap.heap) < k:
                heap.push(val)
            else:
                # 和堆顶的元素进行比较
                
                if val < abs(heap.heap[0]):
                    heap.push(val)
                    # 必须保持定长的序列
                    heap.heap = heap.heap[-k:]
        return sorted( [ abs(i) for i in heap.heap] )

    

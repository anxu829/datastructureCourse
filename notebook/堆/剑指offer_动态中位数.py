# -*- coding:utf-8 -*-


import heapq
# 建立一个最小堆
class minHeap():
    
    def __init__(self):
        self.heap = []
    @classmethod
    def list_init(cls,heaplist):
        temp = cls()
        temp.heap = heaplist
        # heapify 是对于传入的参数的直接处理
        heapq.heapify(temp.heap)
        return temp
        
    def push(self,elm):
        heapq.heappush(self.heap,elm)
    
    def pop(self):
        if len(self.heap) != 0:
            return heapq.heappop(self.heap)
        else:
            return -1

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
            return -1



class Solution:
    def __init__(self):
        # 首先，建立中位数左侧方面的最大堆
        self.maxHeap = maxHeap()
        # 其次，建立中位数右侧方面的最小堆
        self.minHeap = minHeap()

        self.maxHeap.push(-999)
        self.minHeap.push( 999)

    def Insert(self, num):

        # 现在两个堆有数据
        if ( len(self.maxHeap.heap) + len(self.minHeap.heap)  ) % 2 == 0:
            # 目标：插入左侧
            # 首先检查和右侧最小值是否更小
            if num < abs(self.minHeap.heap[0]):
                self.maxHeap.push(num)
            else:
                # 取出右边最小
                temp = abs(self.minHeap.pop())
                self.minHeap.push(num)
                self.maxHeap.push(temp)
        else:
            # 目标插入右侧
            if num > abs(self.maxHeap.heap[0]):
                self.minHeap.push(num)
            else:
                temp = abs(self.maxHeap.pop())
                self.maxHeap.push(num)
                self.minHeap.push(temp)
                
    def GetMedian(self , n =None):
        # write code here
        if (  len(self.maxHeap.heap) + len(self.minHeap.heap) ) % 2 == 0 :
            return (abs(self.maxHeap.heap[0]) + abs(self.minHeap.heap[0]) ) / 2.0 
        else:
            return abs(self.maxHeap.heap[0] )

if __name__ == "__main__":
    lis =[5,2,3,4,1,6,7,0,8]

    test = Solution()
    for val in lis:
        test.Insert(val)
        print(test.GetMedian())

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

    



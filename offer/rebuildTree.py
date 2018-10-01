class Node(object):
    def __init__(self):
        self.data = None
        self.LNode = None
        self.RNode = None 




lis1 = [1 , 2 , 4 ,7 ,3 ,5 ,6  ,8]
lis2 = [4 , 7 , 2 , 1 , 5 , 3 , 8 , 6 ]

def buildTree(lis1, lis2):
    
    if not lis1 and not lis2:
        return None 
        
    root = lis2.index(lis1[0])
    left_2  = lis2[:root]
    left_1  = lis1[1:1 + len(left_2) ]
    right_2 = lis2[root + 1:]
    right_1 = lis1[1 + len(left_2) : ]
    # 如果没有后续内容，则返回空

    node = Node()
    node.data = lis1[0]
    node.LNode = buildTree(left_1,left_2)
    node.RNode = buildTree(right_1,right_2)
    return node


node = buildTree(lis1,lis2)

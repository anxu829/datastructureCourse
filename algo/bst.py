class Node(object):
    def __init__(self):
        self._data = None
        self._lchild = None
        self._rchild = None
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self,data):
        self._data = data 
    
    @property
    def lchild(self):
        return self._lchild
    
    @lchild.setter 
    def lchild(self,node):
        assert type(node) == Node
        self._lchild = node 
        
    
    @property
    def rchild(self):
        return self._rchild
    
    @rchild.setter 
    def rchild(self,node):
        assert type(node) == Node
        self._rchild = node 


class Tree(object):
    def __init__(self):
        self._Node = None
    @property
    def Node(self):
        return self._Node
    
    @Node.setter
    def Node(self,node):
        assert type(node) == Node
        self._Node = node

    def searchBST(self,key):
        def _searchBST(node,key,nodeParent,p):
            if node == None:
                p.append(nodeParent)
                return False 
            else:
                if node.data == key:
                    p.append(nodeParent)
                    return True 
                if node.data < key:
                    return _searchBST(node.rchild,key,node,p)
                if node.data > key:
                    return _searchBST(node.lchild,key,node,p)
        p = []
        status = _searchBST(self.Node,key,None,p)
        return p , status                        

    def insertBSE(self,keys):
        def _insertBSE(key):
            p, status = self.searchBST(key)
            # status 为假，说明这个key没有出现过
            if status == False: 
                n = Node()
                n.data = key

                # 查看是否是根节点
                if not p[0]:
                    self.Node = n   
                else:
                    if key < p[0].data:
                        p[0].lchild = n 
                    elif key > p[0].data:
                        p[0].rchild = n
        for key in keys:
           _insertBSE(key)


    def delteBST(self,key):
        # 首先要查找到位置
        p , status  = self.searchBST(key)
        if status == True:
            node = p[0].lchild if p[0].data > key else p[0].rchild
            if not node.lchild:
                node = node.rchild
            if not node.rchild:
                node = node.lchild
            # step 1 找到第一个没有右节点的子节点和父节点
            parent = node
            child = node.lchild
            while(child.rchild):
                parent = child
                child = child.rchild

            # step2 把node的值替换为child的值
            node.data = child.data 

            if parent == node:
                node.lchild = parent.lchild
            else:
                parent.rchild = child.lchild
            print("remove ", key , " success" )

    # 做一次中序遍历
    def mprint(self):
        def _mprint(node):
            if node.lchild != None:
                _mprint(node.lchild)
            print(node.data,' ',end = '')
            if node.rchild != None:
                _mprint(node.rchild)
        node = self.Node
        _mprint(node)
        




t = Tree()
t.insertBSE([62,58,88,48,73,99,35,51,93,29,37,49,56,36,50])
t.delteBST(48)
t.mprint()




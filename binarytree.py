class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
        
    def printtree(self):
            if self.left:
                self.left.printtree()
            print(self.data)
            if self.right:
                self.right.printtree()
    def inorder(self,k):
        res=[]
        
        if k:
            res.append(k.data)
            res=res +  self.inorder(k.left)
            
            res =res + self.inorder(k.right)

        return res
    def maxdepth(self,k):
        if not k:
            return 0

        else:
            return(1+max(self.maxdepth(k.left),self.maxdepth(k.right)))


k = Node(10)
k.insert(4)
k.insert(12)
k.insert(7)
k.insert(17)
print(k.inorder(k))
print(k.maxdepth(k))
        
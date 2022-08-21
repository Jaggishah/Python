class tree:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.root=data

    def inserting(self,data):
        if self.root:
            if data < self.root:
                if self.left is None:
                    self.left =tree(data)
                else:
                    self.left.insert(data)
            elif data > self.root:
                if self.right is None:
                    self.right =tree(data)
                else:
                    self.right.insert(data)
        else:
            self.root=data
    def printtree(self):
        if self.left:
            self.left.printtree()
        print(self.root,end=" ",sep='-')
        if self.right:
            self.right.printtree()

    def maxdepth(self,obj):
        if not obj:
            return 0
        else:
            return (1+max(self.maxdepth(obj.left),self.maxdepth(obj.right)))

    def inorder(self,obj):
        res=[]
        if obj:
            res = self.inorder(obj.left)
            res.append(obj.root)
            res=res+self.inorder(obj.right)
        return res



obj = tree(3)
obj.inserting(4)
obj.inserting(2)
obj.printtree()
print("transversal=",obj.inorder(obj))
print(obj.maxdepth(obj))

        

                
class Treenode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.appned(child)

    def build_tree(self):
        root = Treenode("Daddy")

        root.add_child("mother")
        root.add_child("sister")
        root.add_child("brother")

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()


j = Treenode()
j.build_tree()
j.print_tree()

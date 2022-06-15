


class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_at_beginining(self,data):
        node = Node(data,self.head)
        self.head=node

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        first=self.head
        while first.next:
            first=first.next

        first.next=Node(data)

    def insert_at_middle(self,data,index):
        first=self.head
        count=0
        while first:
            if count==index-1:
                first.next=Node(data,first.next)
               
            first=first.next
            count+=1

    def print_list(self):
        first=self.head
        llstr=''
        while first:
            llstr += str(first.data) + ' '
            first=first.next
        
        print(llstr)

    def remove(self,index):
        
        if index==0:
            self.head=self.head.next
        

   


root =Linkedlist()
root.insert_at_beginining(5)
root.insert_at_beginining(10)
root.insert_at_middle(7,1)
root.insert_at_middle(7,2)
root.remove(0)
root.print_list()



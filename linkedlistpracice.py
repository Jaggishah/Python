from dataclasses import dataclass


class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class linkedlist:
    def __init__(self):
        self.head=None
    
    def i_a_b(self,data):
        node=Node(data,self.head)
        self.head=node

    def a_end(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        first=self.head
        while first.next:
            first=first.next

        first.next=Node(data,None)



    def printlist(self):
        first=self.head
        ll=""
        while first:
            ll += str(first.data)+"->"
            first=first.next

        print(ll)

j = linkedlist()
j.i_a_b(4)
j.i_a_b(5)
j.a_end(7)
j.printlist()
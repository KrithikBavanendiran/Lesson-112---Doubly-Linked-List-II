class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None

class DoublyLL:
    def __init__(self):
        self.head=None
    
    def searching(self,data):
        t=0
        temp=self.head
        while temp:
            if temp.data==data:
                t=1
                break
            temp=temp.next
        if t==1:
            print("Element found")
        else:
            print("Element not found")
    
    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"-->",end=" ")
                temp=temp.next

l=DoublyLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
l.display()
print(end="\n")
l.searching(20)

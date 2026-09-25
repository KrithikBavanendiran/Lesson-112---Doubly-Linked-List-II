class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
    
class DoublyLL:
    def __init__(self):
        self.head=None

    def insert(self,data,pos):
        nn=Node(data)

        if pos==0:
            nn.next=self.head
            if self.head:
                self.head.prev=nn
            self.head=nn
            return

        temp=self.head

        for i in range(pos-1):
            if temp==None:
                return
            temp=temp.next

        if temp==None:
            return

        nn.next=temp.next
        nn.prev=temp

        if temp.next:
            temp.next.prev=nn

        temp.next=nn

    def display(self):
        if self.head==None:
            print("List is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"--->",end=" ")
                temp=temp.next


l=DoublyLL()

n=Node(10)
l.head=n

n1=Node(20)
n.next=n1
n1.prev=n

n2=Node(30)
n1.next=n2
n2.prev=n1

l.display()
print()

l.insert(100,0)
l.display()
print()

l.insert(200,2)
l.display()
print()

l.insert(300,4)
l.display()
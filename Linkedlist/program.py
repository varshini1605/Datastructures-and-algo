class Node:
    def __init__(self,data):
        self.data=data
        self.next=next
 
class Link:
    def __init__(self):
        self.head=None
      #insert at begining
    def insertAtBegin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    #insert at given index    
    def insertAt(self, data,n):
        new_node = Node(data)
        curr=self.head
        pos=0
        while curr!=None and pos+1 !=n:
                pos=pos+1
                curr=curr.next
        if curr!=None:
            new_node.next=curr.next
            curr.next=new_node
    def printt(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
        
l=Link()
l.insertAtBegin(1)
l.insertAtBegin(2)
l.insertAtBegin(3)
l.insertAt(4,3)
l.printt()

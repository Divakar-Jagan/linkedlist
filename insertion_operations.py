class Node:
  def __init__(self,val):
    self.data=val
    self.next=None
class LinkedList:
  def __init__(self):
    self.head=None
  def display(self):
    if self.head is None:
      print("Linked List is Empty")
    temp=self.head
    while temp is not None:
      print(temp.data,end="-->")
      temp=temp.next
    print("None")
  def insert_end(self,val):
    newnode=Node(val)
    if self.head is None:
      self.head=newnode
    else:
      temp=self.head
      while temp.next is not None:
        temp=temp.next
      temp.next=newnode
  def insert_begin(self,val):
    newnode=Node(val)
    if self.head is None:
      self.head=newnode
    newnode.next=self.head
    self.head=newnode
  def insert_at_pos(self,pos,val):
    newnode=Node(val)
    if pos==1:
      insert_begin(val)
    if pos<1:
      print("Enter Valid Position")
    temp=self.head
    for i in range(1,pos-1):
      temp=temp.next
    newnode.next=temp.next
    temp.next=newnode
  def delete_end(self):
    if self.head is None:
      print("List is Empty")
    temp=self.head
    while temp.next.next is not None:
      temp=temp.next
    temp.next=None
  def delete_begin(self):
    if self.head is None:
      print("List is Empty")
    self.head=self.head.next
  def delete_at_pos(self,pos):
    if self.head is None:
      print("List is Empty")
      return
    if pos==1:
      self.head=self.head.next
      return
    temp=self.head
    for i in range(1,pos-1):
      if temp is None or temp.next is None:
        print("Enter Valid Postion")
        return
      temp=temp.next
      if temp.next is None:
        print("Enter Valid Postion")
        return
      temp.next=temp.next.next
    
list1=LinkedList()

n=int(input())
for i in range(n):
  k=int(input())
  list1.insert_end(k)
list1.display()

num=int(input())
list1.insert_begin(num)
list1.display()

list1.insert_at_pos(5,50)
list1.display()

list1.delete_end()
list1.display()

list1.delete_begin()
list1.display()  

list1.delete_at_pos(4)
list1.display()

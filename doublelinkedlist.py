class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DbLinkedList():
   def __init__(self):
     self.head=None
   def insert_at_begin(self,data):
        node=Node(data)
        if self.head is None:
          self.head=node
          return
        node.next=self.head
        self.head.prev=node
        self.head=node
   def insert_at_end(self,data):
       if self.head is None:
           self.insert_at_begin(data)
           return
       node=Node(data)    
       current=self.head
       while current.next is not None:
           current=current.next
       current.next=node
       node.prev=current 
   def insert_at_position(self,data,position):
       if self.head is None:
           self.insert_at_begin(data)
           return
       if position<=1:
           print("if position between 1,0,-1 we including at the beginig of list")
           self.insert_at_begin(data)
           return
       node=Node(data)
       current: Node=self.head
       for i in range(position-2):
           current=current.next
       nextNode=current.next
       node.next=nextNode
       node.prev=current
       current.next=node
       if nextNode is not None:
           nextNode.prev=node
   def del_at_begin(self): 
    if self.head is None:
     print("No nodes are present")
     return
    firstNode=self.head
    self.head=firstNode.next
    if self.head is None:
        return
    self.head.prev=None
    firstNode.next=None
    
   def del_at_end(self):     
    if self.head is None:
     print("No nodes are present")
     return
    current=self.head
    prev=None
    while current.next is not None:
        prev=current
        current=current.next
    if prev is None:
        self.del_at_begin()
        return
    prev.next=None
    current.prev=None
    current.next=None     
    
   def del_at_pos(self,pos):
      if self.head is None:
       print("No nodes are present")
       return
      if pos<=0:
       print(f'Invalid psotion to delete in the {pos}') 
       return
      if pos==1:
          self.del_at_begin()
          return
      current=self.head
      prev=None
      for i in range(1,pos,1):
          if current.next is None:
              break
          prev=current
          current=current.next
      prev.next=current.next
      if not current.next is None:
          print("hi")
          current.next.prev=current.prev
      current.next=None
      current.prev=None
   
   def search_update_Data(self,search_data,update,newData):
     if self.head is None:
      print("No nodes are present")
      return
     current=self.head
     count=0
     while current is not None:
         count+=1
         if current.data==search_data:
             print(f"{search_data} is found at {count} node in the list")
             if update:
                 if newData:
                  current.data=newData
                  print(f"{search_data} is succesfully updated by {newData} in the node {count}")
                  return
                 else:
                  print("no data ios found to update")
                  return
             return
         current=current.next
   def reverse_list(self):
       if self.head is None:
        print("No nodes are present")
        return
       current=self.head
       prev=None
       while current is not None:
           leftAdd=current.prev
           rightAdd=current.next
           current.prev=rightAdd
           current.next=leftAdd
           prev=current
           current=current.prev
       self.head=prev    
    
   def display(self):
       if self.head is None:
           print("there are no nodes in the list to display please insert the nodes")
           return
       current=self.head
       while current is not None:
             print(current.data)
             current=current.next
        

DBL=DbLinkedList()
DBL.insert_at_begin(10) 
DBL.insert_at_end(20)
DBL.insert_at_end(30) 
DBL.insert_at_end(35) 
DBL.display()    
DBL.reverse_list()
print("after reversing : ")
DBL.display() 
   
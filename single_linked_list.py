# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:18:43 2026

@author: IT
"""
#Nodes creation class

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
#Linked list class

class LinkedList():
   def __init__(self):
       print("satring")
       self.head=None
       
   #Insertion logic begins below
   
   #Insertion at begin code starts
   
   def insertion_at_begin(self,data):
       newNode=Node(data)
       if self.head is None:
           self.head=newNode
           return
       newNode.next=self.head
       self.head=newNode
       
   #Insertion at begin end starts
   
   
   #Insertion at end code starts
   
   def insertion_at_end(self,data):
       newNode=Node(data)
       if self.head is None:
           self.head=newNode
           return
       current=self.head
       while current.next is not None:
           current=current.next
       current.next=newNode
       
   #Insertion at position code starts
   
   def insert_pos(self,data,pos):
       newNode=Node(data)
       if  self.head is None:
           self.insertion_at_begin(data)
           return
       if pos<=0:
           print("there is no position 0 or less than 0 to include please insert in other position")
           return
       if pos==1:
           self.insertion_at_begin(data)
           return
       current=self.head
       for i in range(pos-2):
           current=current.next           
       newNode.next=current.next
       current.next=newNode
        
   #Insertion Logic end here
       
   #Deletion Logic begins below 
   
   #Deletion at begins code starts
   
   def delete_begin(self):
        if self.head is None:
            print("there are no node presents in the list so please insert the nodes in the lined list")
            return
        self.head=self.head.next
        
   #Deletion at begins code end

   #Deletion at end code starts   
   
   def delete_end(self):
       if self.head is None:
           print("there are no node presents in the list so please insert the nodes in the lined list")
           return
       current=self.head
       prev=None
       while current.next is not None:
           prev=current
           current=current.next          
       if current== self.head and prev==None:
           self.head=None
           return
       prev.next=None
       
   #Deletion at end code ends
   
   #Deletion at pos code starts
   
   def delete_pos(self,pos):
       if self.head is None:
           print("there are no node presents in the list so please insert the nodes in the lined list")
           return
       if pos<=0:
            print("there is no position 0 or less than 0 to include please delete in other position")
            return
       if pos==1:
          self.delete_begin()
          return
       current=self.head
       prev=None
       for i in range(pos-1):
           prev=current
           current=current.next
       prev.next=current.next    
       
    #Deletion at pos code ends    
    
   #search data in list code starts
   
   def search_data(self,data):           
        if self.head is None:
             print("there are no node presents in the list so please insert the nodes in the lined list")
             return
        count=0
        current=self.head
        while current is not None:
            count+=1
            if data==current.data:                  
                print(f"data matched in the following node {count} and address is {current}")
                return
            current=current.next
            
   #search data in list code ends   

   #update data in list code starts    
   
   def update_data(self,exsd,newd):
     if self.head is None:
         print("There is no nodes in the linked list to update the data")
         return
     current=self.head
     count=0
     update=None
     while current is not None:
         count+=1
         if current.data==exsd:
             update="found"
             current.data=newd
             print(f"data is updated in the node of {count}")
         current=current.next   
     if update is None:
         print("there isno existing data noe present in this list")
         
   #update data in list code ends  
         
   #reverse list code starts
   
   def reverse_list(self):
       print("harsha")
       if self.head is None:
           print("There are no nodes in the list please  reverlist after insert nodes in the list.")
           return
       current=self.head
       prev=None
       while current is not None:
           next_node=current.next
           current.next=prev
           prev=current
           current=next_node
       self.head=prev     
       
    #reverse list code ends    
   
   def middle_node(self):
       if self.head is None:
           print("There are no nodes in the list please  reverlist after insert nodes in the list.")
           return
       current=self.head
       count=0
       while current is not None:
           count+=1
           current=current.next
       middleposition=count//2
       current=self.head
       for i in range(middleposition):
        current=current.next
        print(f"middle node is {current.data},->{current}")  
        return
       print("If middle nodes to be find the nodes must be three are above three")
       
   def middle_node_pointer(self):
       if self.head is None:
           print("There are no nodes in the list please  reverlist after insert nodes in the list.")
           return
       slow=self.head
       fast=self.head
       while fast and fast.next.next:
            slow=slow.next
            fast=fast.next.next
       
       if slow:
           print(f"The element is middle position is {slow.data} -> {slow}")
       
   #display the list code starts
   def detect_cycle(self):
       if self.head is None:
           print("There are no nodes in the list please  reverlist after insert nodes in the list.")
           return
       slow=self.head
       fast=self.head
       detect=False
       while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print("cycle is detected")
                detect=True
                return
       if not detect :
            print("No detection of cycle")
   def display(self):
        current=self.head
        count=0
        while current is not None:
            print(current.data)
            current=current.next      
            count+=1
        print("length->",count)   
        
  #display the list code ends     
        
L=LinkedList()
L.insertion_at_begin(10)  
L.insertion_at_end(20)  
L.insertion_at_end(30)
L.insertion_at_end(40) 
L.middle_node_pointer()
L.display()
L.middle_node()
L.detect_cycle()

print("head->data",L.head.data)

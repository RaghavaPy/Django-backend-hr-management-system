class Node:
    def __init__(self,data):
        self.data=data
        self.frwd=None
class Queue:
    def __init__(self):
        self.fr=None
        self.rr=None
    def enqueue(self,data):
        if data:
            node=Node(data)
            if node:
                if self.fr is None:
                   self.fr=self.rr=node
                else:
                    self.rr.frwd=node
                    self.rr=node
    def dequeue(self):
        if self.fr is None:
            print("Queue is underflow")
            return
        self.fr=self.fr.frwd     
        if self.fr is None:
            self.rr=None
    def Peek(self):
        if self.fr is None:
             print("Queue is underflow")
             return
        return self.fr.data
    def isEmpty(self):
        if self.fr is None:
            print("Queue is empty") 
            return
        print("Stack is not Empty")
    def rear(self):
           if self.rr is None:
                print("Queue is empty") 
                return   
           return self.rr.data
    def display(self):
        if self.fr is None:
            print("Queue is underflow")
            return
        itiretator=self.fr
        while itiretator is not None:
            print(f"{itiretator.data}")
            itiretator=itiretator.frwd
QQ=Queue()
QQ.enqueue(10)
QQ.enqueue(20)
QQ.enqueue(30)
QQ.enqueue(40)
QQ.enqueue(50)
QQ.enqueue(60)
QQ.display()   
print("dequeu")                  
QQ.dequeue()                   
QQ.display()    
print("dequeu")                  
QQ.dequeue()                   
QQ.display()          
print("dequeu")                  
print(QQ.Peek(),QQ.rear(),QQ.isEmpty) 


class Queue_Array():
    def __init__(self,size):
        self.arr=[0]*size
        self.rear=-1
        self.front=-1
        self.size=size
    def enqueue(self,data):
        if (self.rear+1)%self.size==self.front:
            print("queue is overflow")
            return
        
        if self.front==-1 and self.rear==-1:
            self.front+=1    
        self.rear=(self.rear+1)%self.size
        self.arr[self.rear]=data  
        print(self.rear)
         
    def dequeue(self):
        if self.front==-1:       
            print("Queue is underflow")
            return
        print(f"removed value {self.arr[self.front]}") 
        self.arr[self.front]=None
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        
    def peek(self):
        if self.front==-1:       
            print("Queue is underflow")
            return     
        print(f"peek is {self.arr[self.front]}")
    
    def isEmpty(self):
        if self.front==-1:
            print("Queue is empty")    
            return
    
    def rearELE(self):
        if self.front==-1:       
            print("Queue is underflow")
            return    
        print(f"rear is {self.arr[self.rear]}") 
    
    def display(self):
        if self.front==-1:       
            print("Queue is underflow")
            return    
        i=self.front
        while True:
            print(f"ELEMENT IS :{self.arr[i]}")
            if i==self.rear:
                break
            i=(i+1)%self.size
AQ= Queue_Array(5)
AQ.enqueue(10)
AQ.enqueue(20)
AQ.enqueue(30)
AQ.enqueue(40)
AQ.enqueue(50)
AQ.enqueue(20)   
AQ.display()   
       
       
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=self.next=None
class Deque():
    def __init__(self):
        self.rear=self.front=None
    def enquue_left(self,data):
        if data is not None:
            node=Node(data)
            if node is not None:
                if self.front==None:
                    self.front=self.rear=node
                    return
            node.next=self.front
            self.front.prev=node
            self.front=node
    def enqueue_end(self,data):
        if data is not None:
            node=Node(data)
            if self.front==None:
               self.front=self.rear=node
               return
            node.prev=self.rear
            self.rear.next=node
            self.rear=node
            
    def dequee_left(self):
         if self.front==None:
             print("queue is underfow")
             return
         if self.front==self.rear:
             self.rear=self.front=None
             return
         self.front.next.prev=None
         self.front=self.front.next
         
    def dequee_end(self):
         if self.front==None:
            print("queue is underfow")
            return  
         if self.front==self.rear:
             self.rear=self.front=None        
             return  
         self.rear.prev.next=None
         self.rear=self.rear.prev                 
    def display(self):
        if self.front==None:
            print("queue is underfow")
            return      
        current=self.front
        while True:
            if current:
                print(f"{current.data}")
                current=current.next
            else:
                break    
dq=Deque()
dq.enquue_left(10)
dq.enqueue_end(20)
dq.enqueue_end(30)
dq.display()  
dq.enquue_left(5)
print("srart insert")   
dq.display()  
print("deletion start:")
dq.dequee_left()
dq.display() 
dq.dequee_end()
dq.display() 
                  
import heapq
pq=[]
heapq.heappush(pq,30)
heapq.heappush(pq,10)
heapq.heappush(pq,50)
heapq.heappush(pq,20)
print(pq) 
print(heapq.heappop(pq)) 
print(heapq.heappop(pq))         
print(heapq.heappop(pq))    


mq=[]
heapq.heappush(mq,-30)
heapq.heappush(mq,-20)
heapq.heappush(mq,-50)
heapq.heappush(mq,-60)
print(mq)
print(heapq.heappop(mq)) 
print(heapq.heappop(mq)) 
print(heapq.heappop(mq)) 
print(heapq.heappop(mq))


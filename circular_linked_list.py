# Circular Doubly Linked List

class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    # -------------------- INSERT --------------------

    def insert_at_begin(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.next = self.head
            node.prev = self.head
            return

        current = self.head

        while current.next is not self.head:
            current = current.next

        node.next = self.head
        node.prev = current

        self.head.prev = node
        self.head = node
        current.next = self.head

    def insert_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            node.next = self.head
            node.prev = self.head
            return

        current = self.head

        while current.next is not self.head:
            current = current.next

        node.next = self.head
        node.prev = current

        current.next = node
        self.head.prev = node

    def insert_at_position(self, data, pos):

        if self.head is None:
            print("No nodes are present.")
            return

        if pos <= 0:
            print("Invalid Position")
            return

        if pos == 1:
            self.insert_at_begin(data)
            return

        current = self.head
        prev = None

        for _ in range(pos - 1):

            if current.next is self.head:
                self.insert_at_end(data)
                return

            prev = current
            current = current.next

        node = Node(data)

        node.next = current
        node.prev = prev

        prev.next = node
        current.prev = node

    # -------------------- DELETE --------------------

    def del_at_begin(self):

        if self.head is None:
            print("No nodes are present.")
            return

        first_node = self.head

        if first_node.next is self.head:
            first_node.prev = None
            first_node.next = None
            first_node.data = None
            self.head = None
            return

        current = self.head

        while current.next is not self.head:
            current = current.next

        self.head = first_node.next
        self.head.prev = current
        current.next = self.head

        first_node.prev = None
        first_node.next = None
        first_node.data = None

    def del_at_end(self):

        if self.head is None:
            print("No nodes are present.")
            return

        first_node = self.head

        if first_node.next is self.head:
            first_node.prev = None
            first_node.next = None
            first_node.data = None
            self.head = None
            return

        current = self.head

        while current.next is not self.head:
            current = current.next

        prev = current.prev

        prev.next = self.head
        self.head.prev = prev

        current.prev = None
        current.next = None
        current.data = None

    def del_at_pos(self, pos):

        if self.head is None:
            print("No nodes are present.")
            return

        if pos <= 0:
            print("Invalid Position")
            return

        if pos == 1 or self.node_length() == 1:
            self.del_at_begin()
            return

        current = self.head

        for _ in range(pos - 1):

            if current.next is self.head:
                self.del_at_end()
                return

            current = current.next

        prev = current.prev
        next_node = current.next

        prev.next = next_node
        next_node.prev = prev

        current.prev = None
        current.next = None
        current.data = None
    
    def search_data(self,data,newData):
        if self.head is None:
            print("No nodes are present.")
            return 
        if data:
           count=0
           found=False
           current=self.head
           while True:
               count+=1
               if current.data==data:
                   current.data=newData
                   print(f"Data is found at node {count}")   
                   found=True
                   return
               current=current.next 
               if current is self.head:
                   if not found:
                    print("there is no node with data")    
                    return
        else:
            print("data is null")    
            
    def revrse_list(self):
        if self.head is None:
            print("No nodes are present.")
            return        
        current=self.head
        while True:
            current.prev,current.next=current.next,current.prev
            current=current.prev
            if current is self.head:
                break
        self.head=self.head.next   
         
    # -------------------- UTILITY --------------------

    def node_length(self):

        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:
            count += 1
            current = current.next

            if current is self.head:
                break

        return count
    
    def display(self):

        if self.head is None:
            print("No nodes are present.")
            return

        count = 0
        current = self.head

        while True:
            count += 1
            print(f"Node {count} -> {current.data}")

            current = current.next

            if current is self.head:
                break

        print(f"\nTotal Nodes : {count}")


# -------------------- DRIVER CODE --------------------

cbl = Linked_list()

cbl.insert_at_begin(10)
cbl.insert_at_end(20)
cbl.insert_at_end(30)
cbl.insert_at_end(40)
cbl.display()
cbl.revrse_list()
cbl.display()

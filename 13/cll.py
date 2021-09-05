class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None 
        
    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head
            
    def remove(self,key):
        if self.head.data==key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next 
                    cur = cur.next 
    
    def find_next(self,key):
        if self.head.data == key:
            cur = self.head
            cur = cur.next
            return cur.data
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
                if cur.data == key:
                    cur = cur.next
                    return cur.data
                                    
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break
          



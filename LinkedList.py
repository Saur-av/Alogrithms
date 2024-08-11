class Node:
    def __init__(self,val,next = None) -> None:
        self.val = val
        self.next = next

class SingleLinkList:
    def __init__(self,val = None) -> None:
        self.head = Node(val)
        self.length = 1
    
    def traverse(self): #O(N)
        cur = self.head
        while cur is not None:
            print(cur.val , end = " -> ")
            cur = cur.next
    
    def insert(self,newNode : Node) -> None: #O(N)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = newNode
        self.length += 1

    def insertStart(self,newNode : Node) -> None: #O(1)
        newNode.next = self.head
        self.head = newNode
        self.length +=1
    
    def insertAt(self,newNode:Node,position:int) -> None: #O(P) - P is the position
        if position < 0 or position > (self.length):
            raise IndexError(f"The Given Position is invalid, Valid Ranges are 0 - {self.length}")
        
        if position == 0:
            self.insertStart(newNode)
            return
        
        c = 0
        cur = self.head
        while c != position - 1:
            cur = cur.next
            c += 1

        newNode.next = cur.next
        cur.next = newNode

        self.length += 1
        
    def __str__(self) -> str:
        self.traverse()
        return "\n"
    
    def __repr__(self) -> str:
        self.traverse()
        return "\n"
    
print('Single Linked List: ')
ll = SingleLinkList(1)
print(ll)
ll.insert(Node(2))
print(ll)
ll.insertStart(Node(3))
print(ll)
ll.insertAt(Node(5),3)
print(ll)


class Dnode:
    def __init__(self,val,prev = None, next = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkList:
    def __init__(self,val = None) -> None:
        self.head = Dnode(val)
        self.tail = self.head
        self.length = 1
    
    def traverse(self): #O(N)
        cur = self.head
        while cur is not None:
            print(cur.val, end=" -> ")
            cur = cur.next
    
    def traverseReverse(self):
        cur = self.tail
        while cur is not None:
            print(cur.val, end=" -> ")
            cur = cur.prev
    
    def insert(self,newNode : Dnode) -> None: #O(N)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        
        newNode.prev = cur
        cur.next = newNode
        
        self.tail = newNode
        self.length += 1

    def insertStart(self,newNode : Node) -> None: #O(1)
        self.head.prev = newNode
        newNode.next = self.head
        self.head = newNode
        self.length +=1
    
    def insertAt(self,newNode:Dnode,position:int) -> None: #O(P) - P is the position
        if position < 0 or position > (self.length):
            raise IndexError(f"The Given Position is invalid, Valid Ranges are 0 - {self.length}")
        
        if position == 0:
            self.insertStart(newNode)
            return
        
        if position == self.length:
            self.insert(newNode)
            return
        
        c = 0
        cur = self.head
        while c != position - 1:
            cur = cur.next
            c += 1

        newNode.next = cur.next
        newNode.prev = cur
        cur.next.prev = newNode
        cur.next = newNode

        self.length += 1
       
    def __str__(self) -> str:
        self.traverse()
        return "\n"
    
    def __repr__(self) -> str:
        self.traverse()
        return "\n"
    
print("Doubly LinkedList: ")
dll = DoublyLinkList(1)
print(dll)
dll.insert(Dnode(2))
print(dll)
dll.insertStart(Dnode(3))
print(dll)
dll.insertAt(Dnode(4),3)
print(dll)

print('Reverse Traversal: \n')
dll.traverseReverse()


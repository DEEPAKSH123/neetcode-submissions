class Node:

    def __init__(self,val,key):
        self.val=val
        self.key=key
        self.next=self.prev=None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])# remove from middle
            self.insert(self.cache[key])#insert to right
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(value,key)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            remove=self.left.next
            del self.cache[remove.key]
            self.remove(remove)

    
    def insert(self,node):
        prev=self.right.prev
        prev.next=node
        node.prev=prev
        node.next=self.right
        self.right.prev=node
    
    def remove(self,node):
        prev=node.prev
        next=node.next
        prev.next=next
        next.prev=prev
        node.next=None
        node.prev=None
        

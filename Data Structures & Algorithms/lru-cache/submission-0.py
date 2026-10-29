class Node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=self.prev=None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
        self.map={}
        
    def remove(self,node):
        back=node.prev
        front=node.next
        back.next=front
        front.prev=back
    
    def insertright(self,node):
        front=self.right
        back=self.right.prev
        node.next=front
        node.prev=back
        back.next=node
        front.prev=node

    def get(self, key: int) -> int:
        if key in self.map:
            self.remove(self.map[key])
            self.insertright(self.map[key])
            return self.map[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])
            self.insertright(self.map[key])
            self.map[key].val=value
        else:
            self.map[key]=Node(key,value)
            self.insertright(self.map[key])
            if len(self.map)>self.cap:
                lfu=self.left.next
                self.remove(lfu)
                del self.map[lfu.key]
        
        

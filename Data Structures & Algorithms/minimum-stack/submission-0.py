class MinStack:

    def __init__(self):
        self.stack=[]
        self.minelement=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val=min(val,self.minelement[-1] if self.minelement else val)
        self.minelement.append(val)
        
        

        

    def pop(self) -> None:
        self.stack.pop()
        self.minelement.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minelement[-1]

        

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nums=[]
        stack=[]
        for i in range(len(speed)):
            nums.append((position[i],speed[i]))
        nums.sort(reverse=True)
        for p,s in nums:
            stack.append((target-p)/s)
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)


        
# Last updated: 07/04/2026, 11:40:07
class MyStack:
    from collections import deque

    def __init__(self):

        self.que = deque()

        


        

    def push(self, x: int) -> None:
        self.que.append(x)
        
        

        

    def pop(self) -> int:
        if len(self.que) :
            return self.que.pop()
        return 0
            
        

    def top(self) -> int:
        return self.que[-1]
        

    def empty(self) -> bool:
        return False if  len(self.que) else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
class StockSpanner:

    def __init__(self):
        self.stack = [] # [price, time]
        self.timer = 0
    def next(self, price: int) -> int:

        self.timer += 1

        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()


        res = self.timer 
        if self.stack:
            res = self.timer - self.stack[-1][1]
    
        self.stack.append([price, self.timer])
        
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
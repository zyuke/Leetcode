// https://leetcode.com/problems/stock-price-fluctuation

from sortedcontainers import SortedDict
class StockPrice:

    def __init__(self):
        self.t2price = dict()
        self.p_freq = SortedDict()
        self.cur_t = 0

    def update(self, timestamp: int, price: int) -> None:
        if timestamp > self.cur_t:
            self.cur_t = timestamp
        if timestamp in self.t2price:
            prev_p = self.t2price[timestamp]
            self.p_freq[prev_p] -= 1
            if self.p_freq[prev_p] <= 0:
                del self.p_freq[prev_p]
            
        self.t2price[timestamp] = price
        if price in self.p_freq:
            self.p_freq[price] += 1
        else:
            self.p_freq[price] = 1
        
    def current(self) -> int:
        return self.t2price[self.cur_t]

    def maximum(self) -> int:
        return self.p_freq.peekitem(-1)[0]

    def minimum(self) -> int:
        return self.p_freq.peekitem(0)[0]



# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
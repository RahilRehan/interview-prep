# t.c for lookup => O(1), updating queue => O(1), inserting => O(1)
class LruCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity 
        self.lru = collections.OrderedDict()

    def lookup(self, isbn: int) -> int:
        if isbn not in self.lru:
            return -1
        price = self.lru.pop(isbn)
        self.lru[isbn] = price
        return price
    
    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.lru:
            price = self.lru.pop(isbn)
        elif self.capacity <= len(self.lru):
            self.lru.popitem(last=False)
        self.lru[isbn] = price 

    def erase(self, isbn: int) -> bool:
        return self.lru.pop(isbn, None) is not None
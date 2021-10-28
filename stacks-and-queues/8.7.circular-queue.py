#Best implementation of cirular array queue
# t.c => enque -> O(1) ammortized, deque => O(1)
class Queue:
    SCALE_FACTOR = 2
    def __init__(self, capacity: int) -> None:
        self.q = [None]*capacity
        self.noOfEle = self.head = self.tail = 0

    def enqueue(self, x: int) -> None:
        if self.noOfEle == len(self.q): # then scale the queue
            self.q = self.q[self.head:] + self.q[:self.head] # remove rotation or invalid tail position in queue
            self.head, self.tail = 0, self.noOfEle # reset head and tail, tail instead of rotating moves out of bounds
            self.q += [None]*(len(self.q)*Queue.SCALE_FACTOR - len(self.q)) # scale queue, now tail points to valid location
        self.q[self.tail] = x
        self.tail = (self.tail+1)%len(self.q)
        self.noOfEle += 1

    def dequeue(self) -> int:
        ret = self.q[self.head]
        self.head = (self.head+1)%len(self.q)
        self.noOfEle -= 1
        return ret

    def size(self) -> int:
        return self.noOfEle
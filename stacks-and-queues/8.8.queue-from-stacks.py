class Queue:

    def __init__(self):
        self._enq = []
        self._deq = []

    def enqueue(self, x: int) -> None:
        self._enq.append(x)

    def dequeue(self) -> int:
        if not self._enq and not self._deq:
            raise IndexError("Empty Queue")
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        return self._deq.pop()
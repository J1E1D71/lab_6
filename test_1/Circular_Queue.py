class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayQueue():
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == self._data:
            self._resize = (len(self._data) * 2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def __str__(self):
        return str(self._data)

queue = ArrayQueue()
for i in range(8):
    queue.enqueue(i)
print(queue)  # [0, 1, 2, 3, 4, 5, 6, 7, None, None]
for j in range(5):
    queue.dequeue()
print(queue)  # [None, None, None, None, None, 5, 6, 7, None, None]
for k in range(5):
    queue.enqueue(k + 8)
print(queue)  # [10, 11, 12, None, None, 5, 6, 7, 8, 9]

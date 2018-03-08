class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayDeque:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == len(self._data)

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        else:
            return self._data[(self._front + len(self._data)) % self._size ]

    def delete_first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._data[(self._front + len(self._data)) % self._size]
        self._data[(self._front + len(self._data)) % self._size] = None
        self._front = ((self._front + len(self._data)) % self._size + 1) % len(self._data)
        self._size -= 1
        return answer

    def add_first(self, e):
        if self._front == 0:
            avail = -1
        elif self._front < 0:
            avail = self._front % len(self._data) - 1
        else:
            avail = self._front - 1
        self._data[avail] = e
        self._front = avail
        self._size += 1

    def add_last(self, e):
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def __str__(self):
        return str(self._data)

deque = ArrayDeque()
for i in range(4):
    deque.add_first(i)
print(deque)  # [None, None, None, None, None, None, 3, 2, 1, 0]
for j in range(4):
    deque.add_last(j + 4)
print(deque)  # [4, 5, 6, 7, None, None, 3, 2, 1, 0]
print(deque.delete_first()) # 3
print(deque.delete_last()) # 7

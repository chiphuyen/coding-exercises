import random

from binary_heap import BinaryHeap


class PriorityQueue(object):
    def __init__(self):
        self._heap = BinaryHeap()

    def peek(self):
        return self._heap.peek_min()

    def is_empty(self):
        return self._heap.is_empty()

    def enqueue(self, value):
        self._heap.insert(value)

    def dequeue(self):
        self._heap.extract_min()

    def __iter__(self):
        yield from iter(self._heap)

    def __len__(self):
        return len(self._heap)


def test_priority_queue():
    pq = PriorityQueue()
    values = random.sample(range(-15, 15), 30)
    for v in values:
        pq.enqueue(v)
        print(list(pq))

    for v in iter(pq):
        print(v)


test_priority_queue()

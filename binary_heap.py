'''
A binary heap is a complete binary tree which satisfies
the min-heap ordering property.
The value of each node is greater than or equal to the value of its parent,
with the minimum-value element at the root.

Methods available:
insert(value): insert a value into the binary heap
peek_min(): peek the next smallest value
extract_min(): return the next smallest value and remove it from the heap.
               Raise ValueError if that value doesn't exist
is_empty(): returns True if the heap is empty, False otherwise

Extra usage:
    iter(bh): return iteration to bh
    list(bh): list all values in the heap
              in a pre-order traversal (root, left, right)

BinaryHeap can be used to build a priority queue and to do heap sort algorithm

                insert     extract_min     peek_min
binary heap     O(log n)    O(log n)        O(1)
'''
import random


class BinaryHeap(object):
    def __init__(self, arr=None):
        self._list = [0]
        if arr:
            for value in arr:
                self.insert(value)

    def insert(self, value):
        self._list.append(value)
        self._bubble_up(len(self._list) - 1)

    def peek_min(self):
        if len(self._list) == 1:
            raise ValueError('Empty')
        return self._list[1]

    def extract_min(self):
        if len(self._list) == 1:
            raise ValueError('Empty')
        value = self._list[1]
        self._swap(1, -1)
        self._list = self._list[:-1]
        self._bubble_down(1)
        return value

    def is_empty(self):
        return len(self._list) == 1

    def __len__(self):
        return len(self._list) - 1

    def __iter__(self):
        yield from iter(self._list[1:])

    def _swap(self, idx1, idx2):
        temp = self._list[idx1]
        self._list[idx1] = self._list[idx2]
        self._list[idx2] = temp

    def _bubble_down(self, idx):
        while 2 * idx < len(self._list):  # has at least one child
            if len(self._list) == 2 * idx + 1:
                min_child = 2 * idx
            else:
                if self._list[2 * idx] < self._list[2 * idx + 1]:
                    min_child = 2 * idx
                else:
                    min_child = 2 * idx + 1
            self._swap(min_child, idx)
            idx = min_child

    def _bubble_up(self, idx):
        parent = idx // 2
        while idx > 1 and self._list[idx] < self._list[parent]:
            self._swap(parent, idx)
            idx = parent
            parent = idx // 2


def test_heap():
    bh = BinaryHeap()
    values = random.sample(range(-15, 15), 30)
    for v in values:
        bh.insert(v)
        print(list(bh))

    for v in iter(bh):
        print(v)


test_heap()

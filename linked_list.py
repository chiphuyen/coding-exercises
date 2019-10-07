'''
An unsorted linked list. Nothing fancy here.

Methods available:
insert(value): insert a value into the linked list
remove(value): remove the first occurrence of the value in the list.
                Raise ValueError if that value doesn't exist
Extra usage:
    value in ll: check if a value is in the list
    list(ll): list all values in the list

'''


class Node(object):
    __slots__ = ('value', 'next')

    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def insert(self, value):
        node = Node(value)
        if not self._tail:
            self._head = self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._len += 1

    def remove(self, value):
        node, prev, found = self._find_value(self._head, None, value)
        if not node:
            raise ValueError()
        if prev:
            prev.next = node.next
        else:  # we're removing the head
            self._head = node.next

        if not node.next:  # the node we remove is the tail of the list
            self._tail = prev

        self._len -= 1

    def __contains__(self, value):
        _, _, found = self._find_value(self._head, None, value)
        return found

    def __len__(self):
        return self._len

    def __iter__(self):
        yield from self._iter(self._head)

    def _iter(self, node):
        if node:
            yield node.value
            yield from self._iter(node.next)

    def _find_value(self, curr, prev, value):
        while curr:
            if curr.value == value:
                return curr, prev, True
            prev = curr
            curr = curr.next
        return curr, prev, False


def test_linkedlist():
    ll = LinkedList()
    print(len(ll))
    values = [2, 3, 2, 3, 5, -10]
    for value in values:
        ll.insert(value)
        print(list(ll))
        print(len(ll))

    for value in values:
        ll.remove(value)
        print(list(ll))
        print(len(ll))

    values = [-100, 23, 3, 2, 1, -10]
    for value in values:
        ll.insert(value)
        print(list(ll))
        print(len(ll))


test_linkedlist()

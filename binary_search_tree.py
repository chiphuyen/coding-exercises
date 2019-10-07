'''
This binary search tree allows duplicate values
All values on the left subtree are less than or equal to the root's value.
All values on the right subtree are greater than the root's value.

Methods available:
insert(value): insert a value into the binary search tree
remove(value): remove the first occurrence of the value in the bst.
                Raise ValueError if that value doesn't exist

Extra usage:
    value in bst: check if a value is in the binary search tree
    list(bst): list all values of the tree in an in-order traversal
'''

import random


class Node(object):
    __slots__ = ('value', 'left', 'right')

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BST(object):
    def __init__(self):
        self._root = None
        self._count = 0

    def insert(self, value):
        parent, prev = self._find_parent(self._root, None, value)
        if not parent:
            self._root = Node(value)
        else:
            if value <= parent.value:
                parent.left = Node(value)
            else:
                parent.right = Node(value)
        self._count += 1

    def remove(self, value):
        curr, parent = self._find_parent(self._root, None, value, True)
        if (not curr or curr.value != value):
            raise ValueError()
        if not parent:  # it's the root
            self._root = self._remove_root(self._root, True)
        else:
            if parent.left and parent.left.value == value:
                parent.left = self._remove_root(curr, True)
            else:
                parent.right = self._remove_root(curr, False)
        self._count -= 1

    def __contains__(self, value):
        curr, _ = self._find_parent(self._root, None, value, True)
        return curr and curr.value == value

    def __len__(self):
        return self._count

    def __iter__(self):
        '''
        Traverse the tree in order
        '''
        yield from self._iter(self._root)

    def _remove_root(self, root, left=True):
        if not root.left and not root.right:
            return None
        if not root.left:
            return root.right
        if not root.right:
            return root.left

        prev = root
        if left:
            curr = root.left
            if not curr.right:
                root.value = curr.value
                root.left = curr.left
            else:
                while curr.right:
                    prev = curr
                    curr = curr.right
                root.value = curr.value
                prev.right = curr.left
        else:
            curr = root.right
            if not curr.left:
                root.value = curr.value
                root.right = curr.right
            else:
                while curr.left:
                    prev = curr
                    curr = curr.left
                root.value = curr.value
                prev.left = curr.right
        return root

    def _find_parent(self, node, prev, value, to_remove=False):
        if not node:
            return prev, None

        if to_remove:
            if value == node.value:
                return node, prev

        if value <= node.value:
            if node.left:
                node, prev = self._find_parent(
                    node.left, node, value, to_remove)
            return node, prev

        if node.right:
            node, prev = self._find_parent(node.right, node, value, to_remove)

        return node, prev

    def _iter(self, node):
        if node:
            yield from self._iter(node.left)
            yield node.value
            yield from self._iter(node.right)


def test_bst():
    bst = BST()
    values = []
    for i in range(100):
        value = random.randint(-10, 30)
        values.append(value)
        bst.insert(value)
    assert list(bst) == sorted(values)

    nums = random.sample(values, 40)
    for num in nums:
        bst.remove(num)
        assert len(bst) == len(values) - 1
        bst.insert(num)
        assert len(bst) == len(values)

    assert list(bst) == sorted(values)


test_bst()

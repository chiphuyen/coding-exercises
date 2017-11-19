'''
Implementation of a trie that allows you to remove words

Methods available:
insert(word): insert a value into the trie
remove(word): remove a word from the trie and remove redundant nodes
              Raise ValueError if that value doesn't exist
              If word is only a prefix (not a word), do nothing.
has_prefix(prefix): return True if prefix is a prefix in the trie
has_word(word): return True if word is a word in the trie

Extra usage:
    list(trie): list all the words in the trie
'''

class Node(object):
    __slots__ = ('value', 'marks_end', 'children', 'parent')

    def __init__(self, char=None, end=False, parent=None):
        self.value = char
        self.marks_end = end
        self.children = dict()
        self.parent = parent

    def add_child(self, char, end=False):
        self.children[char] = Node(char, end, self)

    def remove_child(self, char):
        del self.children[char]

    @property
    def num_children(self):
        return len(self.children)

    def __getitem__(self, char):
        return self.children[char]

class Trie(object):
    def __init__(self):
        self._root = Node() # the value of node is None

    def insert(self, word):
        curr = self._root
        for char in word:
            if not char in curr.children:
                curr.add_child(char)
            curr = curr[char]
        curr.marks_end = True

    def remove(self, word):
        found, node = self._find_end_node(word)
        if not found:
            raise ValueError()
        if node.marks_end:
            node.marks_end = False
            self._remove_nodes(node)

    def has_prefix(self, prefix):
        found, _ = self._find_end_node(prefix)
        return found

    def has_word(self, word):
        found, node = self._find_end_node(word)
        return (found and node.marks_end)

    def __iter__(self):
        yield from self._iter(self._root, '')

    def _iter(self, node, prefix):
        if node.marks_end:
            yield prefix
        for child in node.children:
            yield from self._iter(node[child], prefix + child)

    def _find_end_node(self, token):
        curr = self._root
        for char in token:
            if not char in curr.children:
                return False, curr
            curr = curr[char]
        return True, curr

    def _remove_nodes(self, curr):
        if curr.value and curr.num_children == 0:
            curr.parent.remove_child(curr.value)
            self._remove_nodes(curr.parent)


def test_trie():
    trie = Trie()
    words = ['haha', 'you', 'a', 'no', 'hi', 'this', 'verylongword', 'cs2014']
    for word in words:
        trie.insert(word)
        print(list(trie))
    print(trie.has_prefix('hah'))
    print(trie.has_word('hah'))
    print(trie.has_word('haha'))
    print(trie.has_prefix('ab'))
    print(trie.has_prefix(''))
    trie.remove('no')
    trie.remove('haha')
    trie.remove('cs2014')
    print(list(trie))
    print(trie.has_prefix('hah'))
    print(trie.has_word('haha'))
    print(trie.has_prefix('hi'))

test_trie()


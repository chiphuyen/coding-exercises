'''
Algorithms available:
    is_bst(root):
        input: root of a binary tree
        output: True if the binary tree is a binary search tree.
                False otherwise
        The idea is that if it's a binary search tree, when you traverse
        the tree in-order, the values will always be non-decreasing.

        Note that there are two versions of this function.
        The first one is how it should be.
        The second one is the one accepted by HackerRank.
'''


def is_bst(root):
    return _is_bst_helper(root, None)


def _is_bst_helper(node, prev):
    if not node:
        return True
    if not _is_bst_helper(node.left, prev):
        return False
    if prev and prev.data >= node.data:
        return False
    return _is_bst_helper(node.right, node)


def is_bst_hr(root):
    ''' The solution accepted by HackerRank'''
    nodes = _in_order_traversal(root, [])
    prev = None
    seen = set()
    for node in nodes:
        if node.data in seen:
            return False
        if prev and prev >= node.data:
            return False
        seen.add(node.data)


def _in_order_traversal(root, nodes):
    if not root:
        return nodes
    new_nodes = _in_order_traversal(root.left, nodes)
    new_nodes.append(root)
    new_nodes = _in_order_traversal(root.right, new_nodes)
    return new_nodes

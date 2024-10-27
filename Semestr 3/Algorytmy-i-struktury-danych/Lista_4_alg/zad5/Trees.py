
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not (self == other)  # opposite of __eq__

    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):  # works, but O(n^2) worst-case time
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):  # time is linear of subtree
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)  # start _height2 recursion

    def __iter__(self):
        for p in self.positions():  # use the same order as positions()
            yield p.element()  # but yield each element

    def positions(self):
        return self.preorder()  # return the entire preorder iteration

    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):  # start recursion
                yield p

    def _subtree_preorder(self, p):
        yield p  # visit p before its subtrees
        for c in self.children(p):  # for each child c
            for other in self._subtree_preorder(c):  # do preorder of c's subtree
                yield other  # yielding each to our caller

    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):  # start recursion
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):  # for each child c
            for other in self._subtree_postorder(c):  # do postorder of c's subtree
                yield other  # yielding each to our caller
        yield p  # visit p after its subtrees


class BinaryTree(Tree):
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):
        raise NotImplementedError ( 'must be implemented by subclass' )

    def left(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        if self.left(p) is not None:  # if left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p  # visit p between its subtrees
        if self.right(p) is not None:  # if right child exists, traverse its subtree
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        return self.inorder()  # make inorder the default


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = 'element', 'parent', 'left', 'right'

        def __init__(self, element, parent=None, left=None, right=None):
            self.element = element
            self.parent = parent
            self.left = left
            self.right = right

    class Position(BinaryTree.Position):
        def __init__(self, node):
            self.node = node

        def element(self):
            return self.node.element

        def __eq__(self, other):
            return type(other) is type(self) and other.node is self.node

    def _make_position(self, n):
        return self.Position(n)

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = p.node
        return self._make_position(node.parent)

    def left(self, p):
        node = p.node
        return self._make_position(node.left)

    def right(self, p):
        node = p.node
        return self._make_position(node.right)

    def num_children(self, p):
        node = p.node
        count = 0
        if node.left is not None:  # left child exists
            count += 1
        if node.right is not None:  # right child exists
            count += 1
        return count

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = p.node
        if node.left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node.left = self._Node(e, node)  # node is its parent
        return self._make_position(node.left)

    def _add_right(self, p, e):
        node = p.node
        if node.right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node.right = self._Node(e, node)  # node is its parent
        return self._make_position(node.right)

    def _replace(self, p, e):
        node = p.node
        old = node.element
        node.element = e
        return old

    def _delete(self, p):
        node = p.node
        if self.num_children(p) == 2:
            raise ValueError('Position has two children')
        child = node.left if node.left else node.right  # might be None
        if child is not None:
            child.parent = node.parent  # child's grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node  # convention for deprecated node
        return node.element

    def _attach(self, p, t1, t2):
        node = p.node
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be the same type
            raise TypeError('Tree types must match')
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attached t1 as the left subtree of node
            t1._root.parent = node
            node.left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attached t2 as the right subtree of node
            t2._root.parent = node
            node.right = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0


class ExpressionTree(LinkedBinaryTree):
    def __init__(self, token, left=None, right=None):
        super().__init__()  # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token)  # use inherited, nonpublic method
        if left is not None:  # presumably three-parameter form
            if token not in '+-*x/':
                raise ValueError('token must be a valid operator')
            self._attach(self.root(), left, right)  # use inherited, nonpublic method

    def __str__(self):
        pieces = []  # sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))  # leaf value as a string
        else:
            result.append('(')  # opening parenthesis
            self._parenthesize_recur(self.left(p), result)  # left subtree
            result.append(str(p.element()))  # operator
            self._parenthesize_recur(self.right(p), result)  # right subtree
            result.append(')')  # closing parenthesis

    def evaluate(self):
        return self._evaluate_recur(self.root())

    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())  # we assume the element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else:  # treat 'x' or '*' as multiplication
                return left_val * right_val

class BinaryTreeArray:
    DEFAULT_CAPACITY = 10

    class _TreeNode:
        def __init__(self, value, index):
            self._value = value
            self._index = index

        def get_value(self):
            return self._value

        def get_index(self):
            return self._index

        def __str__(self):
            return str(self._value)

    def __init__(self):
        self._array = self.DEFAULT_CAPACITY * [None]

    def set_root(self, value):
        self._array[0] = self._TreeNode(value, 0)
        return self._array[0]

    def get_root(self):
        return self._array[0]

    def add_left_child(self, node, value):
        i = 2 * node.get_index() + 1
        if i > len(self._array):
            self.resize(2 * len(self._array))
        self._array[i] = self._TreeNode(value, i)
        return self._array[i]

    def get_left_child(self, node):
        i = 2 * node.get_index() + 1
        if node.get_index() > len(self._array):
            raise Exception('Index out of range')
        return self._array[i]

    def add_right_child(self, node, value):
        i = 2 * node.get_index() + 2
        if i > len(self._array):
            self.resize(2 * len(self._array))
        self._array[i] = self._TreeNode(value, i)
        return self._array[i]

    def get_right_child(self, node):
        i = 2 * node.get_index() + 2
        if node.get_index() > len(self._array):
            raise Exception('Index out of range')
        return self._array[i]

    def remove_node(self, node):
        self._array[node.get_index()] = None

    def resize(self, capacity):
        new_array = capacity * [None]
        for i in range(min(len(self._array), capacity)):
            new_array[i] = self._array[i]
        self._array = new_array

    def __str__(self):
        result = '|'
        for i in range(len(self._array)):
            if self._array[i] is not None:
                result += str(self._array[i])
            result += '|'
        return result


if __name__ == '__main__':
    tree = BinaryTreeArray()
    root = tree.set_root(5)
    tree.add_left_child(root, 10)
    tree.add_right_child(root, 3)
    n1 = tree.get_left_child(root)
    tree.add_right_child(n1, 2)
    n2 = tree.get_right_child(root)
    tree.add_right_child(n2, 8)
    n3 = tree.get_right_child(n2)
    tree.add_right_child(n3, 12)
    print(tree)

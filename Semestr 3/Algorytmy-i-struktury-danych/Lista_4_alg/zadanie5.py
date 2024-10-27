class BinaryTree:

    def __init__(self, s, left=None, right=None):
        self._left = left
        self._right = right
        self._s = s

    def __str__(self):
        if self._left is None and self._right is None:
            return self._s
        if self._right is None:
            return self._s + '(' + str(self._left) + ')'
        return '(' + str(self._left) + self._s + str(self._right) + ')'

    @staticmethod
    def from_string(s):
        i = 0
        stack = []
        tree = None
        s = s.replace(" ", "")
        while i < len(s):
            if s[i] == '(':
                stack.append(None)
            elif s[i] == ')':
                if not stack:
                    raise Exception('Wrong brackets')
                parent = stack.pop()
                if parent is not None:
                    if parent._left is None:
                        parent._left = tree
                    else:
                        parent._right = tree
                    tree = parent
            elif 'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9':
                token = '' + s[i]
                i += 1
                while i < len(s) and (
                        'a' <= s[i] <= 'z' or 'A' <= s[i] <= 'Z' or '0' <= s[i] <= '9' or s[i] == '.' or s[i] == ','):
                    token += s[i]
                    i += 1
                if (token == 'sin' or token == 'cos' or token == 'exp' or token == 'log') and i < len(s) and s[
                    i] == '(':
                    stack.append(BinaryTree(token))
                else:
                    tree = BinaryTree(token)
                    i -= 1
            else:
                stack.pop()
                new_tree = BinaryTree('' + s[i])
                new_tree._left = tree
                stack.append(new_tree)
                tree = None
            i += 1
        return tree

    def get_differential_tree(self, x):
        if self._s == 'sin':
            return BinaryTree('*', self._left.get_differential_tree(x), BinaryTree('cos', self._left, None))
        elif self._s == 'cos':
            return BinaryTree('*', self._left.get_differential_tree(x),
                              BinaryTree('-', BinaryTree('0'), BinaryTree('sin', self._left, None)))
        elif self._s == 'exp':
            return BinaryTree('*', self._left.get_differential_tree(x), self)
        elif self._s == 'log':
            return BinaryTree('/', self._left.get_differential_tree(x), self._left)
        elif self._s == '+':
            return BinaryTree('+', self._left.get_differential_tree(x), self._right.get_differential_tree(x))
        elif self._s == '-':
            return BinaryTree('-', self._left.get_differential_tree(x), self._right.get_differential_tree(x))
        elif self._s == '*':
            return BinaryTree('+', BinaryTree('*', self._left.get_differential_tree(x), self._right),
                              BinaryTree('*', self._left, self._right.get_differential_tree(x)))
        elif self._s == '/':
            return BinaryTree('/', BinaryTree('-', BinaryTree('*', self._left.get_differential_tree(x), self._right),
                                              BinaryTree('*', self._left, self._right.get_differential_tree(x))),
                              BinaryTree('^', self._right, BinaryTree('2')))
        elif self._s == '^':
            try:
                try:
                    num = int(self._right._s) - 1
                except ValueError:
                    num = float(self._right._s) - 1.0
                if self._right._left is None and self._right._right is None:
                    return BinaryTree('*', self._left.get_differential_tree(x), BinaryTree('*', self._right._s,
                                                                                           BinaryTree('^', self._left,
                                                                                                      BinaryTree(
                                                                                                          str(num)))))
                raise ValueError
            except ValueError:
                raise Exception('Incorrect expression')
        elif self._s == x:
            return BinaryTree('1')
        else:
            return BinaryTree('0')


if __name__ == '__main__':
    expression = '(log(x) +(x/x))'
    my_tree = BinaryTree.from_string(expression)
    print(my_tree)
    diff_tree = my_tree.get_differential_tree('x')
    print(diff_tree)

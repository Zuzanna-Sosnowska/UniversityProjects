from Lista4algorytmy.zad5.Trees import ExpressionTree


def tokenize(raw):
    SYMBOLS = set('+-x*/() ')  # allow for '*' or 'x' for multiplication
    mark = 0
    tokens = []
    n = len(raw)
    for j in range(n):
        if raw[j] in SYMBOLS:
            if mark != j:
                tokens.append(raw[mark:j])  # complete preceding token
            if raw[j] != ' ':
                tokens.append(raw[j])  # include this token
            mark = j + 1  # update mark to be at the next index
    if mark != n:
        tokens.append(raw[mark:n])  # complete preceding token
    return tokens


def build_expression_tree(tokens):
    S = []  # we use list as stack
    for t in tokens:
        if t in '+-x*/':  # t is an operator symbol
            S.append(t)  # push the operator symbol
        elif t not in '()':  # consider t to be a literal
            S.append(ExpressionTree(t))  # push trivial tree storing value
        elif t == ')':  # compose a new tree from three constituent parts
            right = S.pop()  # right subtree as per LIFO
            op = S.pop()  # operator symbol
            left = S.pop()  # left subtree
            S.append(ExpressionTree(op, left, right))  # re-push tree
    # we ignore a left parenthesis
    return S.pop()


def main():
    t = build_expression_tree(tokens=tokenize("(2 + 3)"))


if __name__ == '__main__':
    main()

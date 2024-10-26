from collections.abc import Iterable


class Vector(Iterable):
    def __init__(self, elems=None):
        if elems is None:
            elems = []
        self.__elems = elems

    def __getitem__(self, key):
        return self.__elems[key]

    def __setitem__(self, key, val):
        self.__elems[key] = val

    def __len__(self):
        return len(self.__elems)

    def __iter__(self):
        return self.__elems.__iter__()

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Vector must be of equal length")
        return Vector([a + b for a, b in zip(self, other)])

    def __neg__(self):
        return Vector([-a for a in self.__elems])

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("Vector must be of equal length")
        return Vector([a - b for a, b in zip(self, other)])

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("Vector must be of equal length")
        return Vector([a * b for a, b in zip(self, other)])

    def __rmul__(self, other):
        return Vector([other * a for a in self.__elems])

    def __str__(self):
        comma_list = ''.join([str(a) + ', ' for a in self.__elems])
        return '<' + comma_list[:-2] + '>'

    def append(self, val):
        self.__elems.append(val)


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.__rows = []

    @staticmethod
    def create_from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        m = Matrix(rows, columns)
        for row in list_of_lists:
            m.add_row(Vector(row))
        return m

    @staticmethod
    def identity_matrix(n):
        I = [[1 if i == j  else 0 for i in range(n)] for j in range(n)]
        return Matrix.create_from_list(I)

    def __getitem__(self, item):
        return self.__rows[item]

    def __setitem__(self, key, new_row):
        self.__rows[key] = new_row

    def __str__(self):
        return ''.join([str(row) + '\n' for row in self.__rows])

    def add_row(self, new_row):
        if len(new_row) != self.columns:
            raise ValueError("Matrix rows must be of equal length")
        self.__rows.append(new_row)
        self.rows += 1

    def add_column(self, new_column):
        if len(new_column) != self.rows:
            raise ValueError("Matrix columns must be of equal length")
        for i in range(len(self.rows)):
            self.__rows[i].append(new_column[i])
        self.columns += 1

    def subtract_rows(self, row1, row2):
        self.__rows[row1] -= self.__rows[row2]

    def multiply_row(self, key, scalar):
        self.__rows[key] *= scalar

    def swap_rows(self, row1, row2):
        self.__rows[row1], self.rows[row2] = self.__rows[row2], self.__rows[row1]


def test_vector():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    print(v1)
    print(v2)
    print(v1 + v2)
    for el in v1:
        print(el)
    print(v2 * (2 * v1))

def test_matrix():
    m1 = Matrix.create_from_list([[-1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(m1)

if __name__ == '__main__':
    test_matrix()

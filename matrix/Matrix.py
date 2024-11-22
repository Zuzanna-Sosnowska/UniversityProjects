import copy
from matrix.Vector import Vector


class Matrix:

    def __init__(self):
        self.__rows = []

    @staticmethod
    def from_vectors(vectors):
        m = Matrix()
        for vec in vectors:
            m.add_row(vec)
        return m

    @staticmethod
    def create_from_list(list_of_lists):
        m = Matrix()
        for row in list_of_lists:
            m.add_row(Vector(row))
        return m

    @staticmethod
    def identity_matrix(n):
        I = [[1 if i == j  else 0 for i in range(n)] for j in range(n)]
        return Matrix.create_from_list(I)

    def number_of_rows(self):
        return len(self.__rows)

    def number_of_columns(self):
        return 0 if len(self.__rows) == 0 else len(self.__rows[0])

    def is_empty(self):
        return len(self.__rows) == 0

    def __len__(self):
        return self.number_of_rows() * self.number_of_columns()

    def __getitem__(self, item):
        return self.__rows[item]

    def __setitem__(self, key, new_row):
        self.__rows[key] = new_row

    def __str__(self):
        return ''.join([str(row) + '\n' for row in self.__rows])

    def __rmul__(self, other):
        return Matrix.create_from_list([other * row for row in self.__rows])

    def __sub__(self, other):
        if self.number_of_rows() != other.number_of_rows() and self.number_of_columns() != other.number_of_columns():
            raise ValueError("Matrix has different number of rows and columns")
        res = self.copy()
        for i in range(self.number_of_rows()):
            res[i] -= other[i]

        return res

    def __add__(self, other):
        if self.number_of_rows() != other.number_of_rows() and self.number_of_columns() != other.number_of_columns():
            raise ValueError("Matrix has different number of rows and columns")
        res = self.copy()
        for i in range(self.number_of_rows()):
            res[i] += other[i]

        return res

    def copy(self):
        return Matrix.from_vectors([row.copy() for row in self.__rows])

    def add_row(self, new_row):
        if len(new_row) != self.number_of_columns() and not self.is_empty():
            raise ValueError("Matrix rows must be of equal length")
        self.__rows.append(new_row)

    def add_column(self, new_column):
        if len(new_column) != self.number_of_rows():
            raise ValueError("Matrix columns must be of equal length")
        for i in range(self.number_of_rows()):
            self.__rows[i].append(new_column[i])

    def subtract_rows(self, row1, row2):
        self.__rows[row1] -= self.__rows[row2]

    def multiply_row(self, key, scalar):
        self.__rows[key] *= scalar

    def swap_rows(self, row1, row2):
        self.__rows[row1], self.__rows[row2] = self.__rows[row2], self.__rows[row1]

    def multiply_column(self, column, scalar):
        for row in self.__rows:
            row[column] *= scalar

    def subtract_column(self, index1, index2):
        for row in self.__rows:
            row[index1] -= row[index2]

    def upper_triangular_matrix(self):
        matrix = copy.deepcopy(self)
        if matrix.number_of_rows() == matrix.number_of_columns():
            for j in range(matrix.number_of_columns()):
                find_nullifying_row = False
                for i in range(j, matrix.number_of_rows()):
                    if matrix[i][j] != 0 and find_nullifying_row == False:
                        matrix.swap_rows(i, j)
                        find_nullifying_row = True
                        continue
                    if find_nullifying_row:
                        a = matrix[i][j] / matrix[j][j]
                        matrix[i] = matrix[i] - a * matrix[j]
                if not find_nullifying_row:
                    raise ValueError("Macierz osobliwa")
        return matrix

    def det(self):
        matrix = self.upper_triangular_matrix()
        det = 1
        for i in range(len(self.__rows)):
            det *= matrix[i][i]
        return det

    def multiply_matrix_by_vector(self, vector: Vector) -> Vector:
        if self.number_of_columns() != len(vector):
            raise ValueError("Vector length must be of equal to number of columns in matrix")
        new_vector = Vector()
        for row in self.__rows:
            new_vector.append(sum(row * vector))
        return new_vector

    def inv(self):
        if self.number_of_rows() != self.number_of_columns():
            raise ValueError("Matrix must be of equal length")
        matrix = copy.deepcopy(self)
        n = matrix.number_of_rows()
        I = Matrix.identity_matrix(n)
        for column in range(n):
            find_nullifying_row = False
            for row in range(column, n):
                if matrix[row][column] != 0 and find_nullifying_row == False:
                    matrix.swap_rows(row, column)
                    I.swap_rows(row, column)
                    find_nullifying_row = True
                    continue
                if find_nullifying_row:
                    modifier = matrix[row][column] / matrix[column][column]
                    matrix[row] = matrix[row] - modifier * matrix[column]
                    I[row] = I[row] - modifier * I[column]
            if not find_nullifying_row:
                raise ValueError("Macierz osobliwa")
        for column in range(n - 1, -1, -1):
            for row in range(column):
                modifier = matrix[row][column] / matrix[column][column]
                matrix[row] = matrix[row] - modifier * matrix[column]
                I[row] = I[row] - modifier * I[column]
            modifier = 1 / matrix[column][column]
            I[column] = modifier * I[column]
            matrix[column] = modifier * matrix[column]
        return I

    def norm(self):
        max = 0
        for row in self.__rows:
            if row.norm() > max:
                max = row.norm()
        return max


if __name__ == "__main__":
    A = Matrix.create_from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = Matrix.create_from_list([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    print(A - B)
    print(A)

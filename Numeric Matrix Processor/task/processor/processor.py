import sys
import copy

def get_matrix_from_input():
    print("Enter size of matrix:")
    [row, column] = [int(elem) for elem in input().split()]
    print("Enter matrix:")
    return MyMatrix(row, column)


def get_two_matrices_from_input():
    print("Enter size of first matrix:")
    [row, column] = [int(elem) for elem in input().split()]
    print("Enter first matrix:")
    A = MyMatrix(row, column)
    print("Enter size of second matrix:")
    [row, column] = [int(elem) for elem in input().split()]
    print("Enter second matrix:")
    B = MyMatrix(row, column)
    return [A, B]


class MyMatrix:

    def __init__(self, rows, columns, data_in=None):
        self.rows = rows
        self.columns = columns
        if data_in is not None:
            self.data = data_in
        else:
            self.data = []
            for i in range(int(self.rows)):
                self.data.append((input().split()))
                self.data[i] = [elem for elem in self.data[i]]

    def display(self):
        for i in range(self.rows):
            print(" ".join([str(elem) for elem in self.data[i]]))

    def get_rows(self):
        return self.rows

    def get_columns(self):
        return self.columns

    def data_to_float(self):
        for i in range(int(self.rows)):
            self.data[i] = [float(elem) for elem in self.data[i]]

    def add(self, b):
        self.data_to_float()
        b.data_to_float()
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] += b.data[i][j]

    def multiply_scalar(self, scalar):
        self.data_to_float()
        for i in range(self.rows):
            for j in range(self.columns):
                self.data[i][j] *= scalar

    def check_dims_equal(self, other):
        if self.get_columns() != other.get_columns() \
                and self.get_rows() != other.get_rows():
            print("The operation cannot be performed.")

    def check_dims_multiply(self, other):
        if self.get_columns() != other.get_rows():
            print("The operation cannot be performed.")
            return False
        return True

    def multiply(self, other):
        self.data_to_float()
        other.data_to_float()
        mat_out = []
        for i in range(self.rows):
            row_i = [elem for elem in self.data[i][:]]
            mat_out.append([])
            for j in range(other.columns):
                column_j = [sublist[j] for sublist in other.data]
                mat_out[i].append(0)
                for k in range(self.columns):
                    mat_out[i][j] += row_i[k] * column_j[k]
        print("The result is:")
        for i in range(self.rows):
            print(" ".join([str(float(elem)) for elem in mat_out[i]]))

    def transpose(self, transposition_type):
        mat_out = []
        if transposition_type == "1":
            for j in range(self.rows):
                column_j = [sublist[j] for sublist in self.data]
                mat_out.append(column_j)
            return MyMatrix(self.columns, self.rows, mat_out)
        elif transposition_type == "2":
            for j in range(self.rows - 1, -1, -1):
                column_j = [sublist[j] for sublist in self.data]
                column_j.reverse()
                mat_out.append(column_j)
            return MyMatrix(self.rows, self.columns, mat_out)
        elif transposition_type == "3":
            for j in range(self.rows):
                row_j = [elem for elem in self.data[j]]
                row_j.reverse()
                mat_out.append(row_j)
            return MyMatrix(self.rows, self.columns, mat_out)
        elif transposition_type == "4":
            for j in range(self.rows - 1, -1, -1):
                row_j = [elem for elem in self.data[j]]
                mat_out.append(row_j)
            return MyMatrix(self.columns, self.rows, mat_out)

    def inverse(self):
        det = self.calc_det()
        if det == 0:
            print("This matrix doesn't have an inverse.")
            return
        inverse_matrix = copy.deepcopy(self.data)
        for i in range(self.rows):
            for j in range(self.columns):
                inverse_matrix[j][i] = self.get_cofactor(i, j) / det
        return MyMatrix(self.rows, self.columns, inverse_matrix)

    def calc_det(self):
        if self.rows != self.columns:
            return -1
        if self.rows == 1:
            self.data_to_float()
            return self.data[0][0]
        else:
            sum_det = 0.0
            for i in range(self.columns):
                sum_det += float(self.data[0][i]) * self.get_cofactor(0, i)
            return sum_det

    def get_cofactor(self, row, column):
        if len(self.data[0]) == 1:
            self.data_to_float()
            return self.data[0][0]
        minor = ((-1) ** (row + column))
        data_copy = copy.deepcopy(self.data)
        data_copy.pop(row)
        [j.pop(column) for j in data_copy]
        return minor * MyMatrix(self.rows - 1, self.columns - 1, data_copy).calc_det()

while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    print("Your choice:")
    choice = input()
    if choice == "1":
        [A, B] = get_two_matrices_from_input()
        A.add(B)
        print("The result is:")
        A.display()
    elif choice == "2":
        A = get_matrix_from_input()
        print("Enter constant:")
        in_scalar = int(input())
        A.multiply_scalar(in_scalar)
        print("The result is:")
        A.display()
    elif choice == "3":
        [A, B] = get_two_matrices_from_input()
        if A.check_dims_multiply(B):
            A.multiply(B)
    elif choice == "4":
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        print("Your choice:")
        choice = input()
        A = get_matrix_from_input()
        B = A.transpose(choice)
        B.display()
    elif choice == "5":
        A = get_matrix_from_input()
        print("The result is:")
        print(A.calc_det())
    elif choice == "6":
        A = get_matrix_from_input()
        print("The result is:")
        C = A.inverse()
        C.display()
    elif choice == "0":
        sys.exit()

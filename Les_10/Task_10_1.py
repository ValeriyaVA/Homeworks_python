from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        lenght = len(self.matrix[0])
        for row in self.matrix:
            if len(row) != lenght:
                raise ValueError(f'fail initialization matrix')

    def __str__(self):
        print_matrix = ''
        for i in range(len(self.matrix)):
            if i < len(self.matrix):
                print_matrix += '|' + ' '.join(map(str, self.matrix[i])) + '|\n'
            elif i == len(self.matrix):
                print_matrix += '|' + ' '.join(map(str, self.matrix[i])) + '|'
        return print_matrix

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError('f You can\'t add matrices of different dimensions')
        sum_matrix = [[] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                sum_matrix[i].append(self.matrix[i][j] + other.matrix[i][j])
        return Matrix(sum_matrix)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(second_matrix)
    print(first_matrix + second_matrix)
    # fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])

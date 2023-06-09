#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy
    new_matrix = list(map(lambda i: list(map(lambda x: x ** 2, i)), matrix))

    return new_matrix

import random
import numpy as np
from matplotlib import pyplot as plt
import copy
import math


def load_sudoku(file_name):
    file = open(file_name, "r")
    buff = list(map(int, file.read()))
    return np.reshape(buff, (9, 9))


def fill_sudoku(sudoku):
    app = appearance(sudoku)
    new = copy.copy(sudoku)
    for i in range(9):
        for j in range(9):
            if new[i, j] == 0:
                x = random.randint(1, 9)
                while app[x-1] == 9:
                    x = random.randint(1, 9)
                new[i, j] = x
                app[x-1] += 1
    return new


def appearance_in_row(sudoku, row):
    app = [0 for i in range(9)]
    for i in range(9):
        if sudoku[row-1, i] != 0:
            app[sudoku[row-1, i] - 1] += 1
    return app


def appearance_in_column(sudoku, col):
    app = [0 for i in range(9)]
    for i in range(9):
        if sudoku[i, col-1] != 0:
            app[sudoku[i, col-1] - 1] += 1
    return app


def appearance(sudoku):
    app = [0 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if sudoku[i, j] != 0:
                app[sudoku[i, j] - 1] += 1
    return app


def single_row_energy(sudoku, row):
    app = appearance_in_row(sudoku, row)
    sum = 0
    for i in range(9):
        if app[i] > 0:
            sum += app[i]-1
    return sum


def single_column_energy(sudoku, col):
    app = appearance_in_column(sudoku, col)
    sum = 0
    for i in range(9):
        if app[i] > 0:
            sum += app[i]-1
    return sum


def sudoku_energy(sudoku):
    sum = 0
    for i in range(9):
        sum += single_row_energy(sudoku, i)
        sum += single_column_energy(sudoku, i)
    return sum


def generate_indexes_to_swap(sudoku):
    [i, j] = random.sample(range(9), 2)
    while sudoku[i, j] != 0:
        [i, j] = random.sample(range(9), 2)
    return [i, j]


def solve_sudoku(sudoku):
    filled = fill_sudoku(sudoku)
    curr_energy = sudoku_energy(filled)
    print(curr_energy)
    counter = 0
    restart = 0
    X = []
    Y = []
    for temperature in np.logspace(0, 1, num=1000000)[::-1]:
        counter += 1
        restart += 1
        # if counter % 1000
        [i1, j1] = generate_indexes_to_swap(sudoku)
        [i2, j2] = generate_indexes_to_swap(sudoku)
        while i1 == i2 and j1 == j2:
            [i2, j2] = generate_indexes_to_swap(sudoku)
        # before = single_row_energy(filled, i1) + single_row_energy(filled, i2) + single_column_energy(filled, j1) + single_column_energy(filled, j2)
        filled[i1, j1], filled[i2, j2] = filled[i2, j2], filled[i1, j1]
        # after = single_row_energy(filled, i1) + single_row_energy(filled, i2) + single_column_energy(filled, j1) + single_column_energy(filled, j2)
        # new_energy = curr_energy - before + after
        new_energy = sudoku_energy(filled)
        if math.exp((curr_energy - new_energy)/temperature) > random.random():
            curr_energy = new_energy
        else:
            filled[i1, j1], filled[i2, j2] = filled[i2, j2], filled[i1, j1]
        X.append(counter)
        Y.append(curr_energy)
    print(filled)
    plt.plot(X, Y)
    plt.show()
    print("\n", sudoku_energy(filled))
    print(curr_energy)


sudoku = load_sudoku("sudoku1")
# print(sudoku)
solve_sudoku(sudoku)
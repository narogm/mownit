import random
from matplotlib import pyplot as plt
import matplotlib as mpl
import numpy as np
import math


def generate_image(size, p):
    img = np.array([0 if random.random() > p else 1 for i in range(size * size)])
    return np.reshape(img, (size, size))


def possible(size, i, j):
    if i < 0 or i >= size:
        return False
    if j < 0 or j >= size:
        return False
    return True


# szachownica (4 pkt sasiedztwa)
def energy_I(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in(i-1, i+1):
        for l in(j-1, j+1):
            if possible(size, k, l):
                result += 1 if image[k, l] == 1 else 0
    return result


# pionowe linie (4 pkt sasiedztwa)
def energy_II(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in(i-2, i-1, i+1, i+2):
        if possible(size, k, j):
            result += 1 if image[k, j] == 1 else 0
    # for l in(j-1, j+1):
    #     if possible(size, i, l):
    #         result += 0 if image[i, l] == 1 else -1
    return result


# "wyspy" czarnych punktow (4 pkt sasiedztwa)
def energy_III(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in(i-1, i+1):
        if possible(size, k, j):
            result += 1 if image[k, j] == 1 else 0
    for l in(j-1, j+1):
        if possible(size, i, l):
            result += 1 if image[i, l] == 1 else 0
    return result


# "wyspy" czarnych punktow (8 pkt sasiedztwa)
def energy_IV(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in(i-1, i+1):
        for l in(j-1, j+1):
            if possible(size, k, l):
                result += 1 if image[k, l] == 1 else 0
    for k in(i-1, i+1):
        if possible(size, k, j):
            result += 1 if image[k, j] == 1 else 0
    for l in(j-1, j+1):
        if possible(size, i, l):
            result += 1 if image[i, l] == 1 else 0
    return result


# linie pionowe - czarna obok bialej (16 pkt sasiedztwa)
def energy_V(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in (i-1, i, i+1):
        for l in (j-1, j+1):
            if possible(size, k, l):
                result += -1 if image[k, l] == 1 else 0
    for k in (i-2, i-1, i, i+1, i+2):
        for l in (j-2, j+2):
            if possible(size, k, l):
                result += 1 if image[k, l] == 1 else 0
    return result


def energy_VI(image, size, i, j):
    if image[i, j] == 0:
        return 0
    result = 0
    for k in (i-1, i, i+1):
        for l in (j-1, j+1):
            if possible(size, k, l):
                result += -1 if image[k, l] == 1 else 0
    for k in (i-1, i+1):
        if possible(size, k, j):
            result += -1 if image[k, j] == 1 else 0
    for k in (i-2, i-1, i, i+1, i+2):
        for l in (j-2, j+2):
            if possible(size, k, l):
                result += 1 if image[k, l] == 1 else 0
    for k in (i-2, i+2):
        for l in (j-1, j, j+1):
            if possible(size, k, l):
                result += 1 if image[k, l] == 1 else 0
    return result


def show(image):
    plt.imshow(image, cmap=mpl.cm.Greys)
    plt.show()


def get_image_energy(img, size, energy):
    sum = 0
    for i in range(size):
        for j in range(size):
           sum += energy(img, size, i, j)
    return sum


def simulated_annealing(size, density, energy):
    img = generate_image(size, density)
    curr_energy = get_image_energy(img, size, energy)
    # show(img)
    best = img
    best_energy = curr_energy
    X = []
    Y = []
    counter = 0
    for temperature in np.logspace(0, 1, num=5000000)[::-1]:
        counter += 1
        [i1, j1] = random.sample(range(size), 2)
        [i2, j2] = random.sample(range(size), 2)
        before_swap = energy(img, size, i1, j1) + energy(img, size, i2, j2)
        img[i1, j1], img[i2, j2] = img[i2, j2], img[i1, j1]
        after_swap = energy(img, size, i1, j1) + energy(img, size, i2, j2)
        new_energy = curr_energy + after_swap - before_swap
        if math.exp((new_energy - curr_energy) / temperature) > random.random():
            curr_energy = new_energy
        else:
            img[i1, j1], img[i2, j2] = img[i2, j2], img[i1, j1]
        if best_energy < new_energy:
            best = img
            best_energy = curr_energy
        X.append(counter)
        Y.append(curr_energy)
    show(best)
    plt.plot(X, Y)
    plt.show()


# simulated_annealing(128, 0.5, energy_I)
# simulated_annealing(128, 0.4, energy_II)
# simulated_annealing(128, 0.4, energy_III)
# simulated_annealing(128, 0.4, energy_IV)
# simulated_annealing(128, 0.3, energy_V)
# simulated_annealing(128, 0.3, energy_VI)
# simulated_annealing(512, 0.1, energy_II)
simulated_annealing(512, 0.5, energy_IV)

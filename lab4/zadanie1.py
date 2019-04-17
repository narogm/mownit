import random
import numpy as np
import math
import copy
import matplotlib.pyplot as plt


def show(cities, best, n):
    plt.plot([cities[best[i % n]][0] for i in range(n)], [cities[best[i % n]][1] for i in range(n)], 'xb-')
    plt.show()


def generate_points_to_swap(n, type):
    if type == "arb":
        [i, j] = random.sample(range(n), 2)
    else:
        i = random.randint(0, n-1)
        j = (i+1) % n
    return sorted([i, j])


def get_distance(cities, tour, n, i, j):
    return sum([math.sqrt(sum([(cities[tour[(k + 1) % n]][d] - cities[tour[k % n]][d]) ** 2 for d in [0, 1]])) for k in [j, j-1, i, i - 1]])


def get_whole_distance(cities, tour, n):
    result = 0
    for i in range(n):
        result += get_distance(cities, tour, n, i, (i+1) % n)
    return result


def generate_cities(n):
    return [random.sample(range(100), 2) for i in range(n)]


def generate_4_groups(n):
    result = [[random.randint(15, 35), random.randint(15, 35)] for i in range(n//4)]
    result += [[random.randint(65, 85), random.randint(15, 35)] for i in range(n//4)]
    result += [[random.randint(15, 35), random.randint(65, 85)] for i in range(n//4)]
    result += [[random.randint(65, 85), random.randint(65, 85)] for i in range(n//4)]
    return result


def tsp(n, type, generator):  # type = "arb" (arbitrary swap) else -> type:consecutive swap
    cities = generator(n)
    tour = random.sample(range(n), n)
    best = copy.copy(tour)
    curr_sum = get_whole_distance(cities, tour, n)
    best_sum = get_whole_distance(cities, best, n)
    show(cities, tour, n)
    X = []
    Y = []
    counter = 0
    for temperature in np.logspace(0, 1, num=20000)[::-1]:
        counter += 1
        [i, j] = generate_points_to_swap(n, type)
        new_tour = tour[:i] + tour[j:j+1] + tour[i+1:j] + tour[i:i+1] + tour[j+1:]
        old_distance = get_distance(cities, tour, n, i, j)
        new_distance = get_distance(cities, new_tour, n, i, j)
        if math.exp((old_distance-new_distance)/temperature) > random.random():
            tour = copy.copy(new_tour)
            curr_sum += new_distance-old_distance
        if best_sum > curr_sum:
            best = copy.copy(tour)
            best_sum = curr_sum
        X.append(counter)
        Y.append(curr_sum)
    show(cities, best, n)
    plt.plot(X, Y)
    plt.show()


# tsp(20, "arb", generate_cities)
tsp(20, "con", generate_cities)

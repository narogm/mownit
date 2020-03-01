import math
from scipy import integrate


def fun1(x):
    return math.exp(-x**2)*math.log(x)**2


def fun2(x):
    return 1/(x**3-2*x-5)


def fun3(x):
    return x**5*math.exp(-x)*math.sin(x)


def simpsons(dolna_gr, gorna_gr, n, func):
    h = (gorna_gr - dolna_gr) / n

    x = []
    fx = []

    for i in range(n+1):
        x.append(dolna_gr + i * h)
        fx.append(func(x[i]))

    res = 0
    for i in range(n+1):
        if i == 0 or i == n:
            res += fx[i]
        elif i % 2 != 0:
            res += 4 * fx[i]
        else:
            res += 2 * fx[i]
    res = res * (h / 3)

    return res


dolna_granica = 1
gorna_granica = 5
n = 6
print(simpsons(dolna_granica, gorna_granica, n, fun1))
print(integrate.quad(fun1, dolna_granica, gorna_granica))
print('##############')

# 2 funkcja
dolna_granica = 0
gorna_granica = 1
n = 6
print(simpsons(dolna_granica, gorna_granica, n, fun2))
print(integrate.quad(fun2, dolna_granica, gorna_granica))
print('##############')

# 3 funkcja
dolna_granica = 0
gorna_granica = 1
n = 6
print(simpsons(dolna_granica, gorna_granica, n, fun3))
print(integrate.quad(fun3, dolna_granica, gorna_granica))
print('##############')

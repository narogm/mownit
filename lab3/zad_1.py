# from decimal import getcontext, Decimal
# import numpy as np
# import math
# import mpmath as mp
#
#
# def f1(x):
#     return Decimal(math.cos(x) * math.cosh(x) - 1)
#
#
# def f2(x):
#     #print(x)
#     return Decimal(1) / Decimal(x) - Decimal(math.tan(x))
#
#
# def f3(x):
#     return Decimal(2 ** (-x)) + Decimal(np.exp(x)) + Decimal(2) * Decimal(math.cos(x)) - Decimal(6)
#
#
# def bisection(precision, a, b, epsilon, f):
#     getcontext().prec = precision
#     #epsilon = Decimal(eps)
#
#     while abs(a - b) > epsilon:  # dopóki nie uzyskamy zadanej dokładności
#         #print(a, "----", b)
#         x1 = Decimal((a + b) / 2)
#
#         if abs(f(x1)) <= epsilon:  # jeżeli znaleźliśmy miejsce zerowe mniejsze bądź równe przybliżeniu zera
#             break
#         elif f(x1) * f(a) < 0:
#             b = x1  # nadpisywanie prawego krańca przedziału
#         else:
#             a = x1  # nadpisywanie lewego krańca przedziału
#
#     print(Decimal((a + b) / 2))  # zwracanie znalezionego miejsca zerowego
#
#
# bisection(33, Decimal(3/2*math.pi), Decimal(2*math.pi), 0.05, f1)
# #bisection(33, Decimal(0), Decimal(math.pi/2), 0.05, f2)
# #bisection(33, Decimal(1), Decimal(3), 0.05, f3)
#
# mp.dps = 30
# print(mp.pi)
# print(mp.cos(mp.pi/2))
import matplotlib.pyplot as plt

x0 = 0.5
r = 3.78
dokladnosc = 16

x, y = x0, 0
for _ in range(100):
    next_x = round(r * x * (1 - x), dokladnosc)
    plt.plot([x, x], [y, next_x], color="black")
    plt.plot([x, next_x], [next_x, next_x], color="blue")
    x, y = next_x, next_x
plt.show()
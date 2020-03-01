from scipy import integrate


def fun5(x, y):
    return x**2 + y**2


def doubleIntegral(h, k, lx, ux, ly, uy):
    nx = round((ux - lx) / h + 1)
    ny = round((uy - ly) / k + 1)

    z = [[None for i in range(ny)] for j in range(nx)]
    for i in range(0, nx):
        for j in range(0, ny):
            z[i][j] = fun5(lx + i * h, ly + j * k)

    ax = []
    for i in range(0, nx):
        ax.append(0)
        for j in range(0, ny):

            if j == 0 or j == ny - 1:
                ax[i] += z[i][j]
            elif j % 2 == 0:
                ax[i] += 2 * z[i][j]
            else:
                ax[i] += 4 * z[i][j]
        ax[i] *= (k / 3)

    result = 0
    for i in range(0, nx):
        if i == 0 or i == nx - 1:
            result += ax[i]
        elif i % 2 == 0:
            result += 2 * ax[i]
        else:
            result += 4 * ax[i]
    result *= (h / 3)
    return result


x_dolna, x_gorna = -3, 3
y_dolna, y_gorna = -5, 5
print(doubleIntegral(0.1, 0.1, x_dolna, x_gorna, y_dolna, y_gorna))
print(integrate.dblquad(fun5, x_dolna, x_gorna, lambda x: -5, lambda x: 5))

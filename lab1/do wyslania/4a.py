import matplotlib.pyplot as plt

r = 1.0
X = []
Y = []
while r <= 4:
    x = 0.8543
    for _ in range(300):
        x = (r*x)*(1-x)
    for _ in range(200):
        x = (r*x)*(1-x)
        X.append(r)
        Y.append(x)
    r += 0.02

#ls = '' <- brak lini pomiedzy punktami
#marker = ',' <- zastosowanie malych kropek dla wiekszej czytelnosci wykresu
plt.plot(X, Y, ls='', marker=',', color="black")
plt.show()
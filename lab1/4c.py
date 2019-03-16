r = 4
x = 0.44343
counter = 0

while(x > 0):
    x = x*r*(1-x)
    counter += 1
print(counter)
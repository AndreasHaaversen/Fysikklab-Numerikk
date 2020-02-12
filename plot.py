import matplotlib.pyplot as plt

import calculate

(xy, data) = calculate.calculate()
time_data = calculate.calculate_with_time()

x = xy["x"]
y = xy["y"]

plt.figure('y(x)', figsize=(12, 3))
plt.plot(x, y)
plt.xlabel('$x$', fontsize=20)
plt.ylabel('$y$(x)', fontsize=20)
plt.grid()
plt.show()

for key, value in data.items():
    plt.figure(''+key, figsize=(12, 3))
    plt.plot(x, value)
    plt.xlabel('$x$', fontsize=20)
    plt.ylabel('$' + key + '$(x)', fontsize=20)
    plt.grid()
    plt.show()

for key, value in time_data.items():
    plt.figure(''+key, figsize=(12, 3))
    plt.plot(x, value)
    plt.xlabel('$t$', fontsize=20)
    plt.ylabel('$' + key + '$(t)', fontsize=20)
    plt.grid()
    plt.show()

import matplotlib.pyplot as plt

import calculate

(xy, data) = calculate.calculate()
time_data = calculate.calculate_with_time()

x = xy["x"]
y = xy["y"]

graph_size = (12, 5)

plt.figure('y(x)', figsize=graph_size)
plt.title("Baneform")
plt.plot(x, y)
plt.xlabel('$x$', fontsize=20)
plt.ylabel('$y$(x)', fontsize=20)
plt.grid()
plt.show()

for key, value in data.items():
    plt.figure(''+key, figsize=graph_size)
    plt.title(value[1])
    plt.plot(x, value[0])
    plt.xlabel('$x$', fontsize=20)
    plt.ylabel('$' + key + '$(x)', fontsize=20)
    plt.grid()
    plt.show()

for key, value in time_data.items():
    plt.figure(''+key, figsize=graph_size)
    plt.title(value[1])
    plt.plot(x, value[0])
    plt.xlabel('$t$', fontsize=20)
    plt.ylabel('$' + key + '$(t)', fontsize=20)
    plt.grid()
    plt.show()

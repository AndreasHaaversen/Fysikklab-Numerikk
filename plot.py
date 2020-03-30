import matplotlib.pyplot as plt

import calculate

plt.rcParams.update({'font.size': 20})

(xy, data) = calculate.calculate(selected="hollow_disk")
time_data = calculate.calculate_with_time(selected="hollow_disk")

x = xy["x"]
y = xy["y"]

graph_size = (12, 7)

plt.figure('y(x)', figsize=graph_size)
plt.title("Baneform")
plt.plot(x, y)
plt.xlabel('$x$ [m]', fontsize=20)
plt.ylabel('$y$(x) [m]', fontsize=20)
plt.grid()
plt.show()

for key, value in data.items():
    plt.figure(''+key, figsize=graph_size)
    plt.title(value[1])
    plt.plot(x, value[0])
    plt.xlabel('$x$ [m]', fontsize=20)
    plt.ylabel('$' + key + '$(x)' + " " + value[2], fontsize=20)
    plt.grid()
    plt.show()

plt.figure('Fart som funksjon av tid', figsize=graph_size)
plt.title('Fart som funksjon av tid')
plt.plot(time_data, data["v"][0])
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t)' + " " + value[2], fontsize=20)
plt.grid()
plt.show()

plt.figure('Posisjon som funksjon av tid', figsize=graph_size)
plt.title('Posisjon som funksjon av tid')
plt.plot(time_data, x)
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t)' + " " + value[2], fontsize=20)
plt.grid()
plt.show()

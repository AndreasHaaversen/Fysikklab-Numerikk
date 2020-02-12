import matplotlib.pyplot as plt

import calculate

(xy, data) = calculate.calculate()

x = xy["x"]
y = xy["y"]

plt.plot(x, y)
plt.xlabel('$x$', fontsize=20)
plt.ylabel('$y$(x)', fontsize=20)
plt.grid()
plt.show()

for key, value in data.items():
    plt.plot(x, value)
    plt.xlabel('$x$', fontsize=20)
    plt.ylabel('$' + key + '$(x)', fontsize=20)
    plt.grid()
    plt.show()

import matplotlib.pyplot as plt
import numpy as np
import calculate
from files import *

plt.rcParams.update({'font.size': 20})

(xy, ballData) = calculate.calculate(selected="ball")
ball_time_data = calculate.calculate_with_time(selected="ball")

(xy2, ringData) = calculate.calculate(selected="hollow_disk")
ring_time_data = calculate.calculate_with_time(selected="hollow_disk")

x = xy["x"]

graph_size = (12, 7)

plt.figure('Fart som funksjon av tid', figsize=graph_size)
plt.title("Fart som funksjon av tid")
plt.plot(x, ball_time_data["v_t"][0])
plt.plot(x, ring_time_data["v_t"][0])
plt.legend(["Ball", "Ring"])
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(x) [m/s]', fontsize=20)
plt.grid()
plt.show()

ball_obs_x, ball_obs_y = parse_full(ball_full_path)
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)

plt.figure('Observert mot beregnet ballfart', figsize=graph_size)
plt.title("Fart som funksjon av tid")
plt.plot(x, ball_time_data["v_t"][0])
plt.plot(ball_obs_x, ball_obs_y)
plt.legend(["Beregnet", "Observert"])
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(x) [m/s]', fontsize=20)
plt.grid()
plt.show()

ring_obs_x, ring_obs_y = parse_full(ring_full_path)
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)

plt.figure('Observert mot beregnet ringfart', figsize=graph_size)
plt.title("Fart som funksjon av tid")
plt.plot(x, ball_time_data["v_t"][0])
plt.plot(ring_obs_x, ring_obs_y)
plt.legend(["Beregnet", "Observert"])
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(x) [m/s]', fontsize=20)
plt.grid()
plt.show()

import matplotlib.pyplot as plt
import numpy as np
import os
import calculate

plt.rcParams.update({'font.size': 20})

ball_full_path = "data/FullBane/kulefullbane.txt"
ring_full_path = "data/FullBane/ringfullbane.txt"


def parse_full_x(filename):
    with open(filename, "r") as file:
        whole_file = file.readlines()
        file = whole_file[2:-1]
        X = []
        Y = []
        for line in file:
            clean_line = line.strip("\n").replace(",", ".").split(";")
            X.append(float(clean_line[0]))
            Y.append(float(clean_line[1])/100)

    return X, Y


data = calculate.calculate_with_time(selected="ball")

ts = data
xmin = 0.000
xmax = 1.401
dx = 0.001
x = np.arange(xmin, xmax, dx)

obs_x, obs_y = parse_full_x(ball_full_path)

graph_size = (12, 7)


plt.figure('Posisjon i x-aksen som funksjon av tid', figsize=graph_size)
plt.title("Posisjon i x-aksen som funksjon av tid")
plt.plot(ts, x)
plt.plot(obs_x, obs_y)
plt.legend(["Beregnet posisjon", "Observert posisjon"])
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$x$(t) [m]', fontsize=20)
plt.grid()
plt.show()

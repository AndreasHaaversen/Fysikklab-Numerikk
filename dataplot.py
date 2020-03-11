import matplotlib.pyplot as plt
import os

ball_terminal_speed_path = "data/KuleSluttfart"
ball_full_path = "data/FullBane/kulefullbane.txt"

ring_terminal_speed_path = "data/RingSluttfart"
ring_full_path = "data/FullBane/ringfullbane.txt"

ball_terminal_speed_files = [os.path.join(ball_terminal_speed_path, file) for file in os.listdir(
    ball_terminal_speed_path) if os.path.isfile(os.path.join(ball_terminal_speed_path, file))]

ring_terminal_speed_files = [os.path.join(ring_terminal_speed_path, file) for file in os.listdir(
    ring_terminal_speed_path) if os.path.isfile(os.path.join(ring_terminal_speed_path, file))]


def parse_full(filename):
    with open(filename, "r") as file:
        whole_file = file.readlines()
        file = whole_file[3:-1]
        X = []
        Y = []
        for line in file:
            clean_line = line.strip("\n").replace(",", ".").split(";")
            X.append(float(clean_line[0]))
            Y.append(float(clean_line[3]))

    return X, Y


def parse_terminal(filename):
    with open(filename, "r") as file:
        whole_file = file.readlines()
        line = whole_file[3]
        clean_line = line.strip("\n").replace(",", ".").split(";")
        X = float(clean_line[0])
        Y = float(clean_line[3])

    return X, Y


x, y = parse_full(ball_full_path)

plt.figure('Ball v(t)', figsize=(12, 3))
plt.plot(x, y)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$v$(t)', fontsize=20)
plt.grid()
plt.show()

x, y = parse_full(ball_full_path)

plt.figure('Ring v(t)', figsize=(12, 3))
plt.plot(x, y)
plt.xlabel('$t$', fontsize=20)
plt.ylabel('$v$(t)', fontsize=20)
plt.grid()
plt.show()

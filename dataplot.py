import matplotlib.pyplot as plt
import os
from statistics import variance

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
            Y.append(float(clean_line[3])/100)

    return X, Y


def parse_terminal(filename):
    with open(filename, "r") as file:
        whole_file = file.readlines()
        line = whole_file[3]
        clean_line = line.strip("\n").replace(",", ".").split(";")
        X = float(clean_line[0])
        Y = float(clean_line[3])/100

    return X, Y


def calculate_terminal_variance(filepaths):
    y_list = []
    for path in filepaths:
        X, Y = parse_terminal(path)
        y_list.append(Y)
    return variance(y_list)


def get_terminal_speeds(filepaths):
    y_list = []
    for path in filepaths:
        X, Y = parse_terminal(path)
        y_list.append(Y)
    return y_list


graph_size = (12, 6)

x, y = parse_full(ball_full_path)

plt.figure('Ball v(t)', figsize=graph_size)
plt.title("Ball fart som en funksjon av tid")
plt.plot(x, y)
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.grid()
plt.show()

x, y = parse_full(ring_full_path)

plt.figure('Ring v(t)', figsize=graph_size)
plt.title("Ring fart som en funksjon av tid")
plt.plot(x, y)
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.grid()
plt.show()

box_size = (7, 4)

x = get_terminal_speeds(ball_terminal_speed_files)
plt.figure('Ball terminalfartsvarianse', figsize=box_size)
plt.title("Ball terminalfartsvarianse")
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.boxplot(x)
plt.grid()
plt.show()

x = get_terminal_speeds(ring_terminal_speed_files)
plt.figure('Ring terminalfartsvarianse', figsize=box_size)
plt.title('Ring terminalfartsvarianse')
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.boxplot(x)
plt.grid()
plt.show()

print("Terminal ring variance", calculate_terminal_variance(
    ring_terminal_speed_files))
print("Terminal ball variance", calculate_terminal_variance(
    ball_terminal_speed_files))

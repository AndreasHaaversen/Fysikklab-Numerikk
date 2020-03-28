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
        X.insert(0, 0)
        Y.insert(0, 0)

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

import matplotlib.pyplot as plt
from files import parse_full, parse_terminal, ball_full_path, ring_full_path, get_terminal_speeds, ball_terminal_speed_files, ring_terminal_speed_files, calculate_terminal_variance
plt.rcParams.update({'font.size': 20})


graph_size = (12, 7)

x, y = parse_full(ball_full_path)

plt.figure('Ball v(t)', figsize=graph_size)
plt.title("Ballfart som funksjon av tid")
plt.plot(x, y)
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.grid()
plt.show()

x, y = parse_full(ring_full_path)

plt.figure('Ring v(t)', figsize=graph_size)
plt.title("Ringfart som funksjon av tid")
plt.plot(x, y)
plt.xlabel('$t$ [s]', fontsize=20)
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.grid()
plt.show()

box_size = (9, 4)

x = get_terminal_speeds(ball_terminal_speed_files)
plt.figure('Ball terminalfartsvarianse', figsize=box_size)
plt.title("Ball terminalfartsvarianse")
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.boxplot(x)
plt.xticks([])
plt.grid()
plt.show()

x = get_terminal_speeds(ring_terminal_speed_files)
plt.figure('Ring terminalfartsvarianse', figsize=box_size)
plt.title('Ring terminalfartsvarianse')
plt.ylabel('$v$(t) [m/s]', fontsize=20)
plt.boxplot(x)
plt.xticks([])
plt.grid()
plt.show()

print("Terminal ring variance", calculate_terminal_variance(
    ring_terminal_speed_files))
print("Terminal ball variance", calculate_terminal_variance(
    ball_terminal_speed_files))

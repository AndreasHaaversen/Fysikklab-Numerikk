import numpy as np
from scipy.interpolate import CubicSpline
from ast import literal_eval

g = 9.81

yfast = []


with open("festepunkter.txt") as file:
    fileData = file.read()
    yfast = np.asarray(literal_eval(fileData))

y0 = yfast[0]

h = 0.2
xfast = np.asarray([0, h, 2*h, 3*h, 4*h, 5*h, 6*h, 7*h])

path = CubicSpline(xfast, yfast, bc_type="natural")


objectR = {"ball": 0.0078, "hollow_disk": 0.02475}
R = 0
r = 0.02175
c = 0
M = 0
my = 0


def y(x):
    return path(x)


def derY(x):
    return path(x, 1)


def der2Y(x):
    return path(x, 2)


def v(x):
    return np.sqrt((2*g*(y0-y(x)))/(1+c))


def k(x):
    return abs(der2Y(x))/((1+derY(x)**2)**(3/2))


def sentripitalAcc(x):
    return (v(x)**2)*k(x)


def beta(x):
    return np.arctan(derY(x))


def N(x):
    return M*(g*np.cos(beta(x)) + sentripitalAcc(x))


def a(x):
    return -((g*np.sin(beta(x)))/(1+c))


def staticf(x):
    maxf = abs(N(x))*my
    puref = c*M*a(x)
    f = [-pure if abs(pure) < f else f for pure, f in zip(puref, maxf)]
    return f


def calculate(selected="hollow_disk"):
    global R
    R = objectR[selected]
    objectC = {"ball": 2/5, "hollow_disk": (1 + r**2/R**2)/2}
    objectM = {"ball": 0.016, "hollow_disk": 0.0127}
    objectMy = {"ball": 0.5, "hollow_disk": 0.25}
    global c
    c = objectC[selected]
    global M
    M = objectM[selected]
    global my
    my = objectMy[selected]
    xmin = 0.000
    xmax = 1.401
    dx = 0.001
    x = np.arange(xmin, xmax, dx)
    out = {}
    xy = {}
    xy["x"] = x
    xy["y"] = path(x)
    out["beta"] = (np.degrees(beta(x)), "Banens hellingsvinkel", "[grader]")
    out["k"] = (k(x), "Banekrumning som funksjon av x", "")
    out["v"] = (v(x), "Fart som funksjon av x", "[m/s]")
    out["N"] = (N(x), "Normalkraft som funksjon av x", "[N]")
    out["|f/N|"] = (abs(staticf(x)/N(x)),
                    "Absolutt forhold mellom friksjonskraft og normalkraft", "")
    return (xy, out)


def v_x(x):
    return v(x)*np.cos(beta(x))


def avg_v_x(x1, x2):
    return (1/2)*(v_x(x1) + v_x(x2))


def delta_t(x1, x2, dx):
    return dx/avg_v_x(x1, x2)


def calculate_with_time(selected="ball"):
    global R
    R = objectR[selected]
    objectC = {"ball": 2/5, "hollow_disk": (1 + r**2/R**2)/2}
    objectM = {"ball": 0.016, "hollow_disk": 0.0127}
    objectMy = {"ball": 0.5, "hollow_disk": 0.25}
    global c
    c = objectC[selected]
    global M
    M = objectM[selected]
    global my
    my = objectMy[selected]
    xmin = 0.000
    xmax = 1.401
    dx = 0.001
    x = np.arange(xmin, xmax, dx)
    ts = [delta_t(x[i-1], x[i], dx) for i in range(1, len(x))]
    ts.insert(0, 0)
    return np.cumsum(ts)

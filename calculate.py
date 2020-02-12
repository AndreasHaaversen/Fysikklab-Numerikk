import numpy as np
from scipy.interpolate import CubicSpline
from ast import literal_eval

g = 9.81

yfast = []


with open("festepunkter.txt") as file:
    fileData = file.read()
    yfast = literal_eval(fileData)

y0 = yfast[0]

h = 200
xfast = np.asarray([0, h, 2*h, 3*h, 4*h, 5*h, 6*h, 7*h])

path = CubicSpline(xfast, yfast, bc_type="natural")


# TODO: Replace placeholder value
objectR = {"ball": 0.01, "hollow_disk": 2}
R = objectR["ball"]
r = 1  # TODO: Replace placeholder value


objectC = {"ball": 2/5, "hollow_disk": (1 + r**2/R**2)/2}
objectM = {"ball": 0.016, "hollow_disk": 0.0127}

c = objectC["ball"]
M = objectM["ball"]


def y(x):
    return path(x)


def derY(x):
    return path(x, 1)


def der2Y(x):
    return path(x, 2)


def v(x):
    return np.sqrt((2*g*(y0-y(x)))/(1+c))


def k(x):
    return der2Y(x)/((1+derY(x)**2)**(3/2))


def sentripitalAcc(x):
    return (v(x)**2)*k(x)


def beta(x):
    return np.arctan(derY(x))


def N(x):
    return M*(g*np.cos(beta(x)) + sentripitalAcc(x))


def staticf(x):
    return (c*M*g*np.sin(beta(x)))/(1 + c)


def calculate():
    xmin = 0.000
    xmax = 1.401
    dx = 0.001
    x = np.arange(xmin, xmax, dx)
    out = {}
    out["path"] = path
    out["beta"] = beta(x)
    out["k"] = k(x)
    out["v"] = v(x)
    out["N"] = N(x)
    out["|f/N|"] = abs(staticf(x)/N(x))
    return out


print(calculate())

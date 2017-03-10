import matplotlib.pyplot as plt
from math import sqrt

import numpy as np

color = '#551A8B'
alpha = .65
axes_range = 10
hyperbolas = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x_vals = np.arange(-axes_range, axes_range, 0.001)

# Spacetime interval hyperbolas
for h in hyperbolas:
    # Top hyperbola
    y_vals = [sqrt(x ** 2 + h) for x in x_vals]
    plt.plot(x_vals, y_vals, color=color, alpha=alpha)

    # Bottom hyperbola
    y_vals = [-sqrt(x ** 2 + h) for x in x_vals]
    plt.plot(x_vals, y_vals, color=color, alpha=alpha)

    # Left hyperbola
    x_vals_left = [x for x in x_vals if x <= -sqrt(h)]
    y_vals_top = [sqrt(x ** 2 - h) for x in x_vals_left]
    y_vals_bottom = [-sqrt(x ** 2 - h) for x in x_vals_left]
    plt.plot(x_vals_left, y_vals_top, color=color, alpha=alpha)
    plt.plot(x_vals_left, y_vals_bottom, color=color, alpha=alpha)

    # Right hyperbola
    x_vals_right = [x for x in x_vals if x >= sqrt(h)]
    y_vals_top = [sqrt(x ** 2 - h) for x in x_vals_right]
    y_vals_bottom = [-sqrt(x ** 2 - h) for x in x_vals_right]
    plt.plot(x_vals_right, y_vals_top, color=color, alpha=alpha)
    plt.plot(x_vals_right, y_vals_bottom, color=color, alpha=alpha)


# Speed of light
plt.plot(x_vals, x_vals, color='y', linestyle='dashed', linewidth='2')
plt.plot(x_vals, -x_vals, color='y', linestyle='dashed', linewidth='2')

# Axes
plt.axhline(xmin=-axes_range, xmax=axes_range, color='k')
plt.axvline(ymin=-axes_range, ymax=axes_range, color='k')

plt.axes().set_aspect('equal')
plt.axis([-axes_range, axes_range, -axes_range, axes_range])
plt.minorticks_on()
plt.grid(which='major', linestyle='solid', alpha=.5)
plt.grid(which='minor', alpha=.65)

plt.show()
